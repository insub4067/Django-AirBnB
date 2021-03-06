# Generated by Django 4.0.1 on 2022-01-17 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amenity',
            old_name='createdAt',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='amenity',
            old_name='updatedAt',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='facility',
            old_name='createdAt',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='facility',
            old_name='updatedAt',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='houserule',
            old_name='createdAt',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='houserule',
            old_name='updatedAt',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='createdAt',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='updatedAt',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='createdAt',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='updatedAt',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='roomtype',
            old_name='createdAt',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='roomtype',
            old_name='updatedAt',
            new_name='updated',
        ),
    ]
