# Generated by Django 3.2.11 on 2022-05-02 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netinventory', '0009_changelog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChangeLog',
            new_name='InventoryLog',
        ),
    ]