import os
from django.core.management.base import BaseCommand

from .utils import JSON_FOLDER, BASE_DIR, create_simple_db_data


class Command(BaseCommand):
    """
    Команда для инициализации бд заданными в json файлах начальными данными.
    """
    def handle(self, *args, **options):
        files_list = os.listdir(os.path.join(str(BASE_DIR), JSON_FOLDER))
        if files_list:
            count = 0
            files_count = 0
            for file in files_list:
                if file.split('.')[-1] == 'json':
                    files_count += 1
                    count += create_simple_db_data(file)
            self.stdout.write(self.style.SUCCESS(f'Database initialization was successful.\n'
                                                 f'{count} records in {files_count} instance(s) were added.'))
        else:
            self.stdout.write(self.style.NOTICE('The are no extrernal files with data to operate with.'))
