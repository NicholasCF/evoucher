# Generated by Django 3.1.2 on 2021-01-23 08:27

from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('name', models.CharField(default=django.utils.timezone.now, max_length=128, primary_key=True, serialize=False)),
            ],
        ),
    ]
