# Generated by Django 5.0 on 2024-03-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_event_event_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_photo',
            field=models.ImageField(null=True, upload_to='static'),
        ),
    ]