# Generated by Django 4.2.11 on 2024-03-08 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tab1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('verified', models.BooleanField()),
                ('image', models.ImageField(upload_to='pic')),
            ],
        ),
        migrations.CreateModel(
            name='Whatever',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
