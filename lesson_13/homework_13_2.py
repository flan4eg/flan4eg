import json
import logging

# Настраиваем логирование в файл json_zhuk.log
def my_logger():

    logging.basicConfig(
        filename='json_zhuk.log',
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True
    )
    logger = logging.getLogger('__main__')

    return logger

logger = my_logger()

checking_files = ['swagger.json', 'login.json', 'localizations_ru.json', 'localizations_en.json']
print()

# проверка валидности JSON файлов
for file_name in checking_files:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            file_data = file.read()
            json.loads(file_data)
            print(f"File '{file_name}' is valid JSON.")
            print()
    except json.JSONDecodeError:
        error_message = f"File '{file_name}' is NOT a valid JSON."
        logger.error(error_message)
        print(f"{error_message}")
        print()