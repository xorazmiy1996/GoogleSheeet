import datetime
import gspread
from googleSheet.models import Datas
from xml.etree import ElementTree
import requests


def write():
    sa = gspread.service_account(filename='file.json')

    sh = sa.open("UntitledSpreadsheet")
    wsk = sh.worksheet("test")
    datas = wsk.get_all_records()

    now = datetime.date.today().strftime('%d/%m/%Y')
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + now, stream=True)
    tree = ElementTree.fromstring(response.content)
    for x in tree.iter('Valute'):
        if x.get('ID') == 'R01235':
            worth = x.find('Value').text
            y = worth.replace(',', '.')
            worth = float(y)

    for data in datas:
        rubles = worth * data['стоимость,$']
        date = datetime.datetime.strptime(data['срок поставки'], '%d.%m.%Y').date()
        Datas.objects.update_or_create(order_id=data['заказ №'],
                                       defaults={'order': data['№'], 'order_id': data['заказ №'],
                                                 'price': data['стоимость,$'], 'date': date,
                                                 'price_in_rubles': rubles})
