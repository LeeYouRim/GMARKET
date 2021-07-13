from django.shortcuts import render
from .models import GMarket
from rest_framework import viewsets
from .serializers import GMarketSerializers

# Create your views here.

def index(requets):
    itemlist = GMarket.objects.all()
    return render(requets, "index.html", {"items": itemlist})

class GMarketViewSet(viewsets.ModelViewSet):
    queryset = GMarket.objects.all()
    serializer_class = GMarketSerializers