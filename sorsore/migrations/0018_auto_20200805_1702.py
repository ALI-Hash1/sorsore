# Generated by Django 3.0.8 on 2020-08-05 21:02

import sorsore.blocks.base_blocks
import sorsore.blocks.html_blocks
import sorsore.fields
from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('sorsore', '0017_generalsettings_external_new_tab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselslide',
            name='content',
            field=sorsore.fields.CoderedStreamField([], blank=True),
        ),
        migrations.AlterField(
            model_name='contentwall',
            name='content',
            field=sorsore.fields.CoderedStreamField([], blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='content',
            field=sorsore.fields.CoderedStreamField([], blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='reusablecontent',
            name='content',
            field=sorsore.fields.CoderedStreamField([], blank=True, verbose_name='content'),
        ),
    ]