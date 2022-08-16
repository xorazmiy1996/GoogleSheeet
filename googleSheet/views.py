from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import View

from .models import Datas
from test import write


# Front
class GoogleSheetView(View):
    def get(self, request):
        """We call a function to load the changes in the Google Sheet"""
        write()

        """open the list"""
        date = []
        rubles = []
        data = Datas.objects.all().order_by('order')

        """total amount"""
        total = Datas.objects.all().aggregate(Sum('price'))

        for x in data:
            datestr = x.date.strftime("%m/%d/%Y")
            date.append(datestr)
            rubles.append(x.price_in_rubles)

        context = {
            'data': data, 'rubles': rubles, 'date': date, 'total': total
        }
        return render(request, 'sheet.html', context)




