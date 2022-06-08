# Generated by Django 4.0.5 on 2022-06-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year', models.PositiveSmallIntegerField(verbose_name='Year established')),
                ('ground', models.CharField(max_length=40)),
                ('capacity', models.PositiveIntegerField(blank=True, null=True)),
                ('website', models.URLField(blank=True, max_length=50)),
            ],
        ),
    ]