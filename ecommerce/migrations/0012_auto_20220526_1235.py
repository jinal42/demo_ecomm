# Generated by Django 3.1 on 2022-05-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0011_auto_20220526_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myitem',
            name='price',
            field=models.FloatField(max_length=100),
        ),
    ]