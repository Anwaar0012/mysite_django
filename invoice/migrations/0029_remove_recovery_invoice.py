# Generated by Django 4.2.11 on 2024-04-25 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0028_recovery_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recovery',
            name='invoice',
        ),
    ]
