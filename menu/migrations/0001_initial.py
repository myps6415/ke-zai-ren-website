# Generated by Django 2.2.5 on 2020-01-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField()),
                ('price', models.IntegerField()),
                ('can_sell', models.BooleanField()),
            ],
        ),
    ]
