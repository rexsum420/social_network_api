# Generated by Django 5.0.6 on 2024-06-09 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_active',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
