# Generated by Django 2.0.3 on 2018-05-16 00:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20180515_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessao',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9fbb2b38-21a9-42c8-9439-3082a47d48c5'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]