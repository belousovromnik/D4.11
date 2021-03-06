# Generated by Django 3.0.2 on 2020-01-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(max_length=100, unique=True, verbose_name='ФИО читателя')),
                ('birth_year', models.SmallIntegerField(null=True, verbose_name='Год рождения')),
                ('comment', models.TextField(max_length=100, null=True, unique=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Читатель',
                'verbose_name_plural': 'Читатели',
                'ordering': ['full_name'],
            },
        ),
    ]
