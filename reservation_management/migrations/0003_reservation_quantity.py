# Generated by Django 5.0.4 on 2024-05-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_management', '0002_reservation_returned_alter_reservation_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='quantity',
            field=models.IntegerField(default=False),
        ),
    ]
