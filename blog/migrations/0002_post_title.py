# Generated by Django 2.2 on 2019-04-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=20),
        ),
    ]