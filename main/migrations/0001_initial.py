# Generated by Django 4.0.5 on 2022-06-04 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('message', models.TextField(max_length=256, verbose_name='Сообщение')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Заявки',
                'verbose_name_plural': 'Заявки',
                'ordering': ['-date'],
            },
        ),
    ]
