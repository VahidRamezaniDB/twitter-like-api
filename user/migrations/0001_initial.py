# Generated by Django 3.2.5 on 2021-07-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=35)),
                ('lastName', models.CharField(max_length=55)),
                ('userName', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=86)),
                ('DOB', models.DateField()),
            ],
        ),
    ]
