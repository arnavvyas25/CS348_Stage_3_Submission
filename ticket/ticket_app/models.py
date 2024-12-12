from django.db import models

# Create your models here.

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    table_id = models.IntegerField()
    server_id = models.IntegerField()
    item_id = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['server_id', 'table_id']),  # Composite index
        ]

class Table(models.Model):
    table_id = models.IntegerField(primary_key=True)
    server_id = models.IntegerField()
    num_people = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['server_id']),  # Single index
        ]

class Server(models.Model):
    server_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    station_id = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['station_id']),  # Single index
        ]

class Station(models.Model):
    station_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

