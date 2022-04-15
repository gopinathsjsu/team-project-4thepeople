# Generated by Django 4.0.3 on 2022-04-12 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('state', models.CharField(blank=True, max_length=30)),
                ('zip_code', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=50)),
            ],
        ),
    ]
