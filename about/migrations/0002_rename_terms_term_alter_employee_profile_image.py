# Generated by Django 4.1.7 on 2023-03-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Terms',
            new_name='Term',
        ),
        migrations.AlterField(
            model_name='employee',
            name='profile_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images/about'),
        ),
    ]