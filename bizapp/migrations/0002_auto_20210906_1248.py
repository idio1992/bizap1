# Generated by Django 3.2.7 on 2021-09-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': True, 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'managed': True, 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='img.jpeg', upload_to='shop/'),
        ),
        migrations.AlterModelTable(
            name='category',
            table='Category',
        ),
        migrations.AlterModelTable(
            name='product',
            table='Product',
        ),
    ]
