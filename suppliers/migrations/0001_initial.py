# Generated by Django 4.1.7 on 2023-03-18 18:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('machine_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='models/')),
                ('description', models.TextField(blank=True, null=True)),
                ('machine_link', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('logo_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='models/')),
                ('marketing_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='models/')),
                ('description', models.TextField(blank=True, null=True)),
                ('facts', models.TextField(blank=True, null=True)),
                ('social_facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('social_twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('social_instagram', models.CharField(blank=True, max_length=200, null=True)),
                ('social_youtube', models.CharField(blank=True, max_length=200, null=True)),
                ('social_linkedin', models.CharField(blank=True, max_length=200, null=True)),
                ('social_website', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('web_url', models.URLField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('video_id', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('thumbnail_url', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('product_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='models/')),
                ('description', models.TextField(blank=True, null=True)),
                ('product_link', models.URLField(blank=True, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('machine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suppliers.machine')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='machine',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier'),
        ),
    ]