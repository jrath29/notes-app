# Generated by Django 5.0.3 on 2024-04-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='descricao',
            field=models.TextField(max_length=300),
        ),
    ]
