# Generated by Django 4.2.11 on 2024-04-17 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0009_alter_invoice_id_alter_lineitem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice'),
        ),
    ]
