# Generated by Django 3.1.13 on 2021-08-29 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Facebook Link', null=True)),
                ('twitter', models.URLField(blank=True, help_text='Twitter Link', null=True)),
                ('whatsapp', models.URLField(blank=True, help_text='WhatsApp Link', null=True)),
                ('youtube', models.URLField(blank=True, help_text='YouTube Link', null=True)),
                ('instagram', models.URLField(blank=True, help_text='Instagram Link', null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
