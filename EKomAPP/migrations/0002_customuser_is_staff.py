# Generated by Django 3.1.12 on 2024-12-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EKomAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
