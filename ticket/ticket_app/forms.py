from django import forms
from .models import Order, Table, Server, Item

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_id', 'table_id', 'server_id', 'item_id', 'quantity']
