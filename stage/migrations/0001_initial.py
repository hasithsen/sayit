# Generated by Django 3.1.7 on 2021-08-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(help_text='Enter name of sayer', max_length=200)),
                ('receiver', models.CharField(help_text='Enter name of sayee', max_length=200)),
                ('content', models.CharField(help_text='Enter content to say', max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('least_accessed_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
