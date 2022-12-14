# Generated by Django 4.0.6 on 2022-08-13 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_orders_itemsjson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='itemsJson',
            new_name='items_json',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='orderId',
            new_name='order_id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AddField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(default=422605, max_length=111),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='name',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='orders',
            name='state',
            field=models.CharField(max_length=111),
        ),
    ]
