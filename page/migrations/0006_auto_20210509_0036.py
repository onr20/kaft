# Generated by Django 3.2.2 on 2021-05-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_alter_page_cover_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='carousel')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('deleted', 'Deleted')], default='DEFAULT_STATUS', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('deleted', 'Deleted')], default='DEFAULT_STATUS', max_length=10),
        ),
    ]