# Generated by Django 4.2.11 on 2024-04-30 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_usergame_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('note', models.TextField(max_length=350)),
                ('date', models.DateField(verbose_name='note date')),
            ],
        ),
    ]