# Generated by Django 2.0 on 2019-07-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=158.6, max_digits=20)),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
