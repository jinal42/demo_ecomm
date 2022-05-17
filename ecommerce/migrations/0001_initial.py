# Generated by Django 4.0.4 on 2022-05-12 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=500)),
                ('price', models.CharField(max_length=100)),
                ('cloth_image', models.ImageField(default='/home/ts/Documents/j/demo_ecomm/ecomm/ecommerce/static/ecommerce/images/home/product1.jpg', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('gender', models.CharField(default='female', max_length=15)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]