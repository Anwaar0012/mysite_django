# Generated by Django 4.2.11 on 2024-04-16 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0008_alter_invoice_total_amount_alter_lineitem_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]