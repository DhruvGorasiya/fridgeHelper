# Generated by Django 4.1.8 on 2023-04-19 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FridgeManager', '0002_credential_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
    ]