# Generated by Django 4.1.7 on 2023-03-22 17:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_special_image_alter_stat_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('image', models.ImageField(blank=True, null=True, upload_to='images/displays/home')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
