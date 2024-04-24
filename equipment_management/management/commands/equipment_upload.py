from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
import pandas as pd
from equipment_management.models import Equipment  # Adjust this import to your app and model

class Command(BaseCommand):
    help = 'Imports data from an Excel file into the Equipment database'

    def handle(self, *args, **options):
        # Define the path to your Excel file
        file_path = Path('path/to/your/media/folder/equipment.xlsx')
        if not file_path.exists():
            raise CommandError(f'File {file_path} does not exist')

        # Read the Excel file
        df = pd.read_excel(file_path, engine='openpyxl')

        # Helper function to map location
        def map_location(location):
            location_mapping = {
                'XRLab Blue Cabinet': 'blue_cabinet',
                'XRLab Blue Cabinet Large': 'blue_cabinet_large',
                'XRLab Medium Wooden Cabinet': 'medium_wooden_cabinet',
                'Other': 'other',
            }
            return location_mapping.get(location, 'other')

        # Iterate through rows and create database entries
        for index, row in df.iterrows():
            Equipment.objects.create(
                equipmentName=row['Device Name'],
                equipmentType=row['Device Type'],
                quantity=row['Quantity'],
                auditDate=row['Audit'],
                location=map_location(row['Location']),
                equipmentStatus=row['Status'] if pd.notna(row['Status']) else 'Available',
                accessLevel='', 
                serialNo='',     
                comments=row['Comments'] if pd.notna(row['Comments']) else ''
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported data from Excel file.'))
