# Generated by Django 3.1.13 on 2021-09-04 14:37

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('helpcenter', '0006_auto_20210904_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='common_questions',
            field=wagtail.core.fields.StreamField([('commonly_asked_questions', wagtail.core.blocks.StructBlock([('category', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('questions_and_answer', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('paragraph', wagtail.core.blocks.TextBlock(max_length=200, required=True))])))]))], null=True),
        ),
    ]
