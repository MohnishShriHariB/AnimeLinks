# Generated by Django 4.2.3 on 2023-07-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('disc', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('link', models.URLField(blank=True)),
            ],
        ),
    ]
