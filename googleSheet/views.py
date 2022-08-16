from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import View

import datetime
import gspread
from xml.etree import ElementTree
import requests

from .models import Datas
from test import write


# Front
class GoogleSheetView(View):
    def get(self, request):
        write()
        date = []
        rubles = []
        data = Datas.objects.all()
        total = Datas.objects.all().aggregate(Sum('price'))

        for x in data:
            datestr = x.date.strftime("%m/%d/%Y")
            date.append(datestr)
            rubles.append(x.price_in_rubles)
        context = {
            'data': data, 'rubles': rubles, 'date': date, 'total': total
        }
        return render(request, 'sheet.html', context)

    # def write_to_database(self):
    #     sa = gspread.service_account(filename='../file.json')
    #     sh = sa.open("UntitledSpreadsheet")
    #     wsk = sh.worksheet("test")
    #     datas = wsk.get_all_records()
    #
    #     now = datetime.date.today().strftime('%d/%m/%Y')
    #     response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + now, stream=True)
    #     tree = ElementTree.fromstring(response.content)
    #     for x in tree.iter('Valute'):
    #         if x.get('ID') == 'R01235':
    #             worth = x.find('Value').text
    #             y = worth.replace(',', '.')
    #             worth = float(y)
    #
    #     for data in datas:
    #         rubles = worth * data['стоимость,$']
    #         date = datetime.datetime.strptime(data['срок поставки'], '%d.%m.%Y').date()
    #
    #         Datas.objects.update_or_create(order_id=data['заказ №'],
    #                                        defaults={'order': data['№'], 'order_id': data['заказ №'],
    #                                                  'price': data['стоимость,$'], 'date': date,
    #                                                  'price_in_rubles': rubles})
    #



