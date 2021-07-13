from rest_framework import serializers
from .models import GMarket

class GMarketSerializers(serializers.ModelSerializer):
    class Meta:
        model = GMarket
        fields = ('__all__')