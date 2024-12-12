from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from ticket_app.models import *
from ticket_app.forms import OrderForm
from django.urls import reverse_lazy

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

    def form_valid(self, form):
        return super().form_valid(form)

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)