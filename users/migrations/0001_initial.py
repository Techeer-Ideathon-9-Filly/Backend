# Generated by Django 5.0.1 on 2024-05-31 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('nickname', models.CharField(max_length=20)),
            ],
        ),
    ]
