# Generated by Django 2.2.14 on 2020-09-30 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]
