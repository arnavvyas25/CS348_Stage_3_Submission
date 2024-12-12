from django.contrib import admin

# Register your models here.
from ticket_app.models import *

admin.site.register(Table)
admin.site.register(Server)
admin.site.register(Item)
admin.site.register(Station)
admin.site.register(Order)