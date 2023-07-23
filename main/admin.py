from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'message', 'date')
    list_display_links = ('id', 'name', 'date')
    search_fields = ('name', 'phone', 'date')


admin.site.register(Order, OrderAdmin)
