# Generated by Django 4.1.7 on 2023-04-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_usernet_bio_usernet_birthday_usernet_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernet',
            name='gender',
            field=models.CharField(choices=[('W', 'Женский'), ('N', 'Нет'), ('M', 'Мужской')], default='N', max_length=1),
        ),
    ]
