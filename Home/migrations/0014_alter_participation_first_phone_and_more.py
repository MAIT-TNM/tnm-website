# Generated by Django 5.0 on 2024-03-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_alter_event_event_id_alter_participation_p_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='first_phone',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='participation',
            name='fourth_phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='participation',
            name='second_phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='participation',
            name='third_phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
