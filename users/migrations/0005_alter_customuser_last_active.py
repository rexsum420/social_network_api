# Generated by Django 5.0.6 on 2024-06-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_last_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_active',
            field=models.CharField(default='.', max_length=512),
        ),
    ]
