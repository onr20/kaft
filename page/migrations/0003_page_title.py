# Generated by Django 3.2.2 on 2021-05-08 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_page_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(default='title', max_length=200),
            preserve_default=False,
        ),
    ]
