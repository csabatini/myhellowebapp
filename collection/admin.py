from django.contrib import admin
from collection.models import Stock


class StockAdmin(admin.ModelAdmin):
    model = Stock
    list_display = ('symbol', 'name',)
    prepopulated_fields = {'slug': ('symbol',)}

admin.site.register(Stock, StockAdmin)
