from django.forms import ModelForm
from collection.models import Stock

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ('symbol', 'name')