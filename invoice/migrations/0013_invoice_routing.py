# Generated by Django 4.2.11 on 2024-04-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0012_invoice_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='routing',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]