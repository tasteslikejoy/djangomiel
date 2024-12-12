import os
from django.core.management.base import BaseCommand

from .utils import JSON_FOLDER, BASE_DIR, clear_db_data


class Command(BaseCommand):
    """Команда для очистки всех данных из моделей бд заполняемых при инициализации."""
    def handle(self, *args, **options):
        files_list = os.listdir(os.path.join(str(BASE_DIR), JSON_FOLDER))
        if files_list:
            count = 0
            for file in files_list:
                if file.split('.')[-1] == 'json':
                    count += clear_db_data(file)
            self.stdout.write(self.style.SUCCESS(f'{count} records was successfully deleted from database.'))
        else:
            self.stdout.write(self.style.NOTICE('The are no extrernal files with data operate with.'))
        pass
        # count = clear_role_db()
        # self.stdout.write(self.style.SUCCESS(
        #     f'{count} records deleted from the database.\nЗаписи Ролей в количестве {count} шт. удалены из базы данных.'))
        #
        # self.stdout.write(self.style.SUCCESS(
        #     'Initialize db command executed successfully.\nКоманда инициализации базы данных выполнена успешно.'))

