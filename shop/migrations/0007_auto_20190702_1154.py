# Generated by Django 2.0 on 2019-07-02 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190702_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]