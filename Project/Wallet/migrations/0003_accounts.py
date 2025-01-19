# Generated by Django 5.1.5 on 2025-01-18 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0002_outcome_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=255)),
                ('money_save', models.CharField(max_length=255)),
                ('money_out', models.CharField(max_length=255)),
                ('money_total', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]
