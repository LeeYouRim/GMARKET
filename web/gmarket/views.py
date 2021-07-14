from django.shortcuts import render
from .models import GMarket
from rest_framework import viewsets
from .serializers import GMarketSerializers
import xlwt
from django.http import  HttpResponse
from django.utils.timezone import now


# Create your views here.

def index(requets):
    itemlist = GMarket.objects.all()
    return render(requets, "index.html", {"items": itemlist})

class GMarketViewSet(viewsets.ModelViewSet):
    queryset = GMarket.objects.all()
    serializer_class = GMarketSerializers

def excel_export(request):
    response = HttpResponse(content_type="application/vnd.ms-excel")
    response['Content-Disposition'] = 'attachment; filename="gmarket.xls"'
    
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('gmarket')
    row_num = 0
    col_names = ['title', 'price', 'sale', 'brand', 'day']
    for idx, col_name in enumerate(col_names):
        ws.write(row_num, idx, col_name)
    
    rows = GMarket.objects.all().values_list('title', 'price', 'sale', 'brand', 'create_at')
    for row in rows:
        row_num +=1
        for col_num, attr in enumerate(row):
            ws.write(row_num, col_num, attr)

    wb.save(response)
    return response
