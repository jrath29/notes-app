# Generated by Django 5.0.3 on 2024-04-09 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_alter_nota_descricao'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nota',
            new_name='Note',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='descricao',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='titulo',
            new_name='title',
        ),
    ]