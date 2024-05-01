from django.shortcuts import render
from . forms import ReportForm
from reportlab.pdfgen import canvas
from django.core.files.base import ContentFile
from io import BytesIO
from datetime import timedelta
from django.http import HttpResponse
from .models import Report, Reservation, Equipment
from django.utils import timezone
from django.db.models import Count



def report_manager(request):
    reports = Report.objects.all()  # Fetch all equipment items from the database
    return render(request, 'report_management/reportmanagement.html', {'reports': reports})




def generate_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        # Validate the form input
        if form.is_valid():
            report_type = form.cleaned_data['report_type']
            buffer = BytesIO() # Buffer to hold PDF data
            p = canvas.Canvas(buffer) # Creates the PDF object/page
            p.setTitle(f'{report_type} Report') # Sets PDF title/name
            y_position = 800

            # Generate the report based on the selected report type which is picked in the .html page and passed to the view
            if report_type == 'overdue_equipment':
                today = timezone.now().date()
                # Checks for reservations that are "overdue" based on the current date vs the expected return date
                overdue_reservations = Reservation.objects.filter(expectedReturnDate__lt=today)
                for reservation in overdue_reservations:
                    # Prints/adds the overequipment details to the PDF
                    p.drawString(100, y_position, f"ID: {equipment.id}, Name: {equipment.equipmentName}, Expected Return: {reservation.expectedReturnDate}")
                    y_position -= 20 # Jumps to the next line
                    # Checks if the current page is full and create a new page if it is
                    if y_position < 100:
                        p.showPage()
                        y_position = 800

            # Generate an "Audit Status" report
            elif report_type == 'audit_status':
                one_year_ago = timezone.now().date() - timedelta(days=365)
                overdue_audits = Equipment.objects.filter(auditDate__lt=one_year_ago)
                for equipment in overdue_audits:
                    p.drawString(100, y_position, f"ID: {equipment.id}, Name: {equipment.equipmentName}, Last Audit: {equipment.auditDate}")
                    y_position -= 20
                    if y_position < 100:
                        p.showPage()
                        y_position = 800

            # Handle "Inventory Status" report
            elif report_type == 'inventory_status':
                all_equipment = Equipment.objects.all()
                for equipment in all_equipment:
                    p.drawString(100, y_position, f"ID: {equipment.id}, Name: {equipment.equipmentName}, Status: {equipment.equipmentStatus}")
                    y_position -= 20
                    if y_position < 100:
                        p.showPage()
                        y_position = 800

            # Generate an "Equipment Usage" report
            elif report_type == 'equipment_usage':
                equipment_usage = Reservation.objects.values('equipment').annotate(usage_count=Count('equipment'))
                for item in equipment_usage:
                    equipment_id = item['equipment']
                    usage_count = item['usage_count']
                    equipment = Equipment.objects.get(id=equipment_id)
                    p.drawString(100, y_position, f"ID: {equipment.id}, Name: {equipment.equipmentName}, Usage Count: {usage_count}")
                    y_position -= 20
                    if y_position < 100:
                        p.showPage()
                        y_position = 800

            p.showPage()
            p.save() # Save PDF file
            buffer.seek(0)  # resets the buffer position

            # Create a new Report instance and attach the PDF file
            report = Report()
            report.name = f"{report_type} Report"
            report.report_type = report_type
            report.date_created = timezone.now()
            filename = f"{report_type}_report_{timezone.now().strftime('%Y%m%d')}.pdf"
            buffer.seek(0)
            report.pdf.save(filename, ContentFile(buffer.read()))
            report.save()

            # Prepare the PDF file response
            response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
        else:
            # If the form is not valid, render the form again
            return render(request, 'generate_report.html', {'form': form})
    else:
        # If not a POST request, show the empty form to generate a report
        form = ReportForm()
        return render(request, 'generate_report.html', {'form': form})
