# Generated by Django 3.1.2 on 2021-03-18 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0005_remove_voucher_code_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='code_list',
            field=models.FileField(blank=True, null=True, upload_to='codes'),
        ),
    ]