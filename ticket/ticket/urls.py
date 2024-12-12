"""
URL configuration for ticket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ticket_app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('order/add/', OrderCreateView.as_view(), name='order_add'),
    path('order/edit/<int:pk>/', OrderUpdateView.as_view(), name='order_edit'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path('orders-by-server/<int:server_id>/', OrdersByServerView.as_view(), name='orders_by_server'),
    path('tables-by-server/<int:server_id>/', TablesByServerView.as_view(), name='tables_by_server'),
    path('items-by-station/<int:station_id>/', ItemsByStationView.as_view(), name='items_by_station'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
