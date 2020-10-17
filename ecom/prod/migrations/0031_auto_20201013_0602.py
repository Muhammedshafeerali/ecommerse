# Generated by Django 3.1.2 on 2020-10-13 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod', '0030_auto_20201009_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('Acessories', 'Acessories'), ('Apparel', 'Apparel')], max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('pant', 'pant'), ('jeans', 'jeans'), ('t-shirt', 't-shirt'), ('shirt', 'shirt'), ('shoe', 'shoe'), ('sunglass', 'sunglass')], max_length=300),
        ),
    ]