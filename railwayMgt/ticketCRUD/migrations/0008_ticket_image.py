# Generated by Django 3.1.7 on 2021-04-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketCRUD', '0007_auto_20210422_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
