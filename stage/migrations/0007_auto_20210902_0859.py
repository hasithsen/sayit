# Generated by Django 3.1.7 on 2021-09-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0006_message_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='votes',
        ),
        migrations.AddField(
            model_name='message',
            name='views',
            field=models.IntegerField(default=0, null=True),
        ),
    ]