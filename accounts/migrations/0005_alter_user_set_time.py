# Generated by Django 3.2.7 on 2022-06-07 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_company_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='set_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]