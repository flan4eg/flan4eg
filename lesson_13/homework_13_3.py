import logging
import xml.etree.ElementTree as ET

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)
logger = logging.getLogger('__main__')


def find_number(file_path: str, group_number: str) -> str:
    tree = ET.parse(file_path)
    root = tree.getroot()

    for group in root.findall('group'):
        number_element = group.find('number')

        if number_element is not None and number_element.text == group_number:
            incoming_element = group.find('timingExbytes/incoming')

            if incoming_element is not None:
                return incoming_element.text

    # Возвращаем None, если совпадений не найдено
    return None

group_number = "4"

users_data = find_number('groups.xml', group_number)

if users_data:
    logger.info(f"For group with number '{group_number}' value 'incoming' is: {users_data}")
else:
    logger.info(f"Value 'incoming' for group '{group_number}' is NOT found.")