# Generated by Django 3.1.13 on 2021-09-04 09:09

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='Phone',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='contact_person',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='email',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
    ]