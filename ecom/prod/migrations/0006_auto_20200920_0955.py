# Generated by Django 3.1.1 on 2020-09-20 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod', '0005_auto_20200920_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]
