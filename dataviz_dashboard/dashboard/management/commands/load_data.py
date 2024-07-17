# dashboard/management/commands/load_data.py
import json
from datetime import datetime
from django.core.management.base import BaseCommand
from dashboard.models import Data  # Adjust the import based on your actual model

class Command(BaseCommand):
    help = 'Load data from JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                try:
                    # Convert datetime strings to datetime objects
                    added = datetime.strptime(item['added'], '%B, %d %Y %H:%M:%S')
                    published = datetime.strptime(item['published'], '%B, %d %Y %H:%M:%S')

                    # Extract year and save as IntegerField
                    start_year = added.year
                    end_year = published.year

                    # Create Data object with validated fields
                    Data.objects.create(
                        start_year=start_year,
                        end_year=end_year,
                        intensity=int(item['intensity']),
                        sector=item['sector'],
                        topic=item['topic'],
                        insight=item['insight'],
                        url=item['url'],
                        region=item['region'],
                        impact=int(item['impact']),
                        added=added,
                        published=published,
                        country=item['country'],
                        relevance=int(item['relevance']),
                        pestle=item['pestle'],
                        source=item['source'],
                        title=item['title'],
                        likelihood=int(item['likelihood'])
                    )
                except ValueError as e:
                    self.stderr.write(self.style.WARNING(f"Skipping entry due to error: {e}"))
                    continue  # Skip this entry and proceed to the next

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
