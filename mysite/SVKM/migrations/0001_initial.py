# Generated by Django 5.1 on 2024-08-22 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                #id is auto created (primary key) (auto incremented)
                ('question_text', models.CharField(max_length=200)),
                ('noOfQuestion', models.IntegerField()),
                ('put_date', models.DateTimeField(verbose_name='date Published')),
            ],
        ),
    ]
