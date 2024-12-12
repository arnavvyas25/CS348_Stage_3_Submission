# Generated by Django 5.1.2 on 2024-11-04 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0002_alter_item_item_id_alter_server_server_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('table_id', models.IntegerField()),
                ('server_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='table_id',
        ),
    ]