# Generated by Django 5.1 on 2024-08-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SVKM', '0002_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeename', models.CharField(max_length=200)),
                ('employeeDesignation', models.CharField(max_length=100)),
                ('employeeSalary', models.IntegerField()),
            ],
        ),
    ]
