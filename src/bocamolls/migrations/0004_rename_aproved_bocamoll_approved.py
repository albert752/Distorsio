# Generated by Django 4.0 on 2021-12-31 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bocamolls', '0003_bocamoll_creation_alter_bocamoll_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bocamoll',
            old_name='aproved',
            new_name='approved',
        ),
    ]
