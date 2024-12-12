import json
from os.path import join as path_join
from pathlib import Path
from django.apps import apps


JSON_FOLDER = 'files_for_filling_db'
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
APP_BASE_MODELS_LABEL = 'showcase'


def get_json(name_json_file):
    """Вспомогательная функция для открытия JSON файла и передачи его содержимого."""
    with open(path_join(JSON_FOLDER, name_json_file), 'r', encoding='utf-8') as file:
        result_data = json.load(file)
        return result_data


def get_model_name(name_json_file):
    """Возвращает имя модели базы данных основываясь на названии JSON файла"""
    return name_json_file.split('.')[0].lower().capitalize()


def create_simple_db_data(name_json_file) -> int:
    """Функция для наполнения бд данными из файла JSON, если в модели еще нет данных.
    Возвращает количество созданных записей. Алгоритм для баз данных с одинаковой структурой."""
    model = apps.get_model(
        app_label=APP_BASE_MODELS_LABEL,
        model_name=get_model_name(name_json_file)
    )
    if not model.objects.count():
        data = get_json(name_json_file=name_json_file)
        count = 0
        for instance in data:
            model(
                **instance
            ).save()
            count += 1
        return count


def clear_db_data(name_json_file) -> int:
    """Функция для очистки тоблицы по иени файла JSON. Возвращает количество удалённых записей."""
    model = apps.get_model(
        app_label=APP_BASE_MODELS_LABEL,
        model_name=get_model_name(name_json_file)
    )
    count = model.objects.count()
    model.objects.all().delete()
    return count
