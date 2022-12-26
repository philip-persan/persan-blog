# Generated by Django 4.1.4 on 2022-12-26 15:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
