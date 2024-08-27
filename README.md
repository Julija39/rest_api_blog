# Открываем и читаем содержимое файлов models.py и app.py
file_path_models = "/mnt/data/models.py"
file_path_app = "/mnt/data/app.py"

with open(file_path_models, 'r', encoding='utf-8') as file:
    models_content = file.read()

with open(file_path_app, 'r', encoding='utf-8') as file:
    app_content = file.read()

models_content, app_content[:500]  # Отображаем первые 500 символов файла app.py и весь файл models.py

