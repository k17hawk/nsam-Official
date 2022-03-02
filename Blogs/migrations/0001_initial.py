# Generated by Django 3.1 on 2020-08-12 06:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('publishBy', models.CharField(blank=True, max_length=100, null=True)),
                ('Blog_by', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(default='', max_length=150)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='Blog/images')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
