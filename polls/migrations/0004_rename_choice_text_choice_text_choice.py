# Generated by Django 5.0.3 on 2025-03-02 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_text_choice_choice_choice_text_choice_voters'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='text_choice',
        ),
    ]
