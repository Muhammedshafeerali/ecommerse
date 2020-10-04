# Generated by Django 3.1.2 on 2020-10-02 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod', '0013_auto_20201002_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('Apparel', 'Apparel'), ('Acessories', 'Acessories')], max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('t-shirt', 't-shirt'), ('shoe', 'shoe'), ('jeans', 'jeans'), ('shirt', 'shirt'), ('pant', 'pant'), ('sunglass', 'sunglass')], max_length=300),
        ),
    ]
