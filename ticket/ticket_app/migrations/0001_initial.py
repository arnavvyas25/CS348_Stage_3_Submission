# Generated by Django 5.1.2 on 2024-11-04 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('station_id', models.IntegerField()),
                ('table_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('server_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('station_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('table_id', models.AutoField(primary_key=True, serialize=False)),
                ('server_id', models.IntegerField()),
                ('num_people', models.IntegerField()),
            ],
        ),
    ]
