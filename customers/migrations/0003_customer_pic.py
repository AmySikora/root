# Generated by Django 4.2.19 on 2025-03-19 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='customers'),
        ),
    ]
