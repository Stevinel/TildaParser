# Generated by Django 4.2.5 on 2023-11-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customer_is_receive_mails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='is_receive_mails',
            field=models.BooleanField(default=True, verbose_name='Получает рассылку'),
        ),
    ]