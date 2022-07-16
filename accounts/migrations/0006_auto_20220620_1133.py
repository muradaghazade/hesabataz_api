# Generated by Django 3.2.7 on 2022-06-20 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_set_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='expences',
        ),
        migrations.RemoveField(
            model_name='company',
            name='income',
        ),
        migrations.AddField(
            model_name='user',
            name='expence',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='income',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Income',
                'verbose_name_plural': 'Incomes',
            },
        ),
        migrations.CreateModel(
            name='Expence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expences', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Expence',
                'verbose_name_plural': 'Expences',
            },
        ),
    ]