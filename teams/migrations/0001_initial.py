# Generated by Django 3.1.13 on 2021-08-29 14:41

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('Country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
                'managed': True,
            },
        ),
    ]
