# Generated by Django 4.0.10 on 2024-06-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='update_at',
            field=models.DateField(),
        ),
    ]
