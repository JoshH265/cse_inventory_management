from django.shortcuts import render
from home.views import homepage
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
        if form.is_valid():
            report_type = form.cleaned_data['report_type']
            buffer = BytesIO()
            p = canvas.Canvas(buffer)
            p.setTitle(f'{report_type} Report')
            y_position = 800

            if report_type == 'overdue_equipment':
                today = timezone.now().date()
                overdue_reservations = Reservation.objects.filter(expectedReturnDate__lt=today)
                for reservation in overdue_reservations:
                    equipment = reservation.equipment
                    p.drawString(100, y_position, f"ID: {equipment.id}, Name: {equipment.equipmentName}, Expected Return: {reservation.expectedReturnDate}")
                    y_position -= 20
                    if y_position < 100:
                        p.showPage()
                        y_position = 800

            elif report_type == 'audit_status':
                one_year_ago = timezone.now().date() - timedelta(days=365)
                overdue_audits = Equipment.objects.filter(auditDate__lt=one_year_ago)
                for equipment in overdue_audits:
                    p.drawString(100, y_position, f"ID: {equipment.id}, Name: {equipment.equipmentName}, Last Audit: {equipment.auditDate}")
                    y_position -= 20
                    if y_position < 100:
                        p.showPage()
                        y_position = 800

            elif report_type == 'inventory_status':
                all_equipment = Equipment.objects.all()
                for equipment in all_equipment:
                    p.drawString(100, y_position, f"ID: {equipment.id}, Name: {equipment.equipmentName}, Status: {equipment.equipmentStatus}")
                    y_position -= 20
                    if y_position < 100:
                        p.showPage()
                        y_position = 800
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
            p.save()
            buffer.seek(0)  # Go to the start of the BytesIO buffer

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
            return render(request, 'generate_report.html', {'form': form})
    else:
        form = ReportForm()
        return render(request, 'generate_report.html', {'form': form})
