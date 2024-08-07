# Generated by Django 5.0.6 on 2024-07-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва')),
                ('task', models.TextField(max_length=500, verbose_name='Завдання')),
                ('date_task', models.DateField(verbose_name='Дата завдання')),
                ('date_result', models.DateField(verbose_name='Дата виконання')),
                ('status', models.CharField(max_length=9, verbose_name='Статус')),
            ],
        ),
    ]
