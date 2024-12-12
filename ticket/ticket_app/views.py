from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from ticket_app.models import *
from ticket_app.forms import OrderForm
from django.urls import reverse_lazy
from ticket_app.queries import Queries

# Create your views here.

def home(request):
    orders = Order.objects.all()
    tables = Table.objects.all()
    servers = Server.objects.all()
    stations = Station.objects.all()
    items = Item.objects.all()

    context = {
        'Orders': orders,
        'Tables': tables,
        'Servers': servers,
        'Stations': stations,
        'Items': items,
    }
    return render(request, 'home.html', context)


def about(request):
 return render(request, 'about.html')

def order_form(request):
    return render(request, 'order_form.html', {
        'form': OrderForm()
    })

def order_confirm_delete(request):
    return render(request, 'order_confirm_delete.html')

class OrderCreateView(CreateView):
    model = Order
    fields = ['table_id', 'server_id', 'item_id', 'quantity']
    template_name = 'order_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)

class OrderUpdateView(UpdateView):
    model = Order
    fields = ['table_id', 'server_id', 'item_id', 'quantity']
    template_name = 'order_edit.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Order.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)
    
# prepared statements
def orders_by_server(request, server_id):
    orders = Queries.get_orders_by_server_id(server_id)
    return render(request, 'orders_list.html', {'orders': orders})

def tables_by_server(request, server_id):
    tables = Queries.get_tables_by_server_id(server_id)
    return render(request, 'tables_list.html', {'tables': tables})

def items_by_station(request, station_id):
    items = Queries.get_items_by_station_id(station_id)
    return render(request, 'items_list.html', {'items': items})

class OrdersByServerView(TemplateView):
    template_name = 'orders_list.html'

    def get(self, request, server_id, *args, **kwargs):
        orders = Order.objects.filter(server_id=server_id)
        context = {'orders': orders, 'server_id': server_id}
        return render(request, self.template_name, context)

class TablesByServerView(TemplateView):
    template_name = 'tables_list.html'

    def get(self, request, server_id, *args, **kwargs):
        tables = Table.objects.filter(server_id=server_id)
        context = {'tables': tables, 'server_id': server_id}
        return render(request, self.template_name, context)

class ItemsByStationView(TemplateView):
    template_name = 'items_list.html'

    def get(self, request, station_id, *args, **kwargs):
        items = Item.objects.filter(station_id=station_id)
        context = {'items': items, 'station_id': station_id}
        return render(request, self.template_name, context)