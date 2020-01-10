# Generated by Django 2.0 on 2019-07-02 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190702_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='last_name',
        ),
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.EmailField(default=True, max_length=254),
        ),
    ]