import xml.etree.ElementTree as ET
from .models import Currency
import requests
from django_q.tasks import schedule


def parse_xml_task():
    api_url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(api_url)

    if response.status_code == 200:
        xml_data = response.text

        root = ET.fromstring(xml_data)

        for element in root.iter('Valute'):
            numcode = element.find('NumCode').text
            charcode = element.find('CharCode').text
            nominal = element.find('Nominal').text
            name = element.find('Name').text
            value = element.find('Value').text
            vunitrate = element.find('Value').text

            defaults = dict(
                numcode=numcode,
                charcode=charcode,
                nominal=int(nominal),
                name=name,
                value=float(value.replace(',', '.')),
                vunitrate=float(vunitrate.replace(',', '.'))
            )
            Currency.objects.update_or_create(defaults,
                                              numcode=numcode)

        print("Данные успешно сохранены в базе данных.")

    else:
        print(
            f"Ошибка при получении данных. Код ответа: {response.status_code}")


schedule('currency.tasks.parse_xml_task', q_options={
    'timeout': 600}, schedule_type='M', repeats=-1)
