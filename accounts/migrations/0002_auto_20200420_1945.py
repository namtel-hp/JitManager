# Generated by Django 2.2.6 on 2020-04-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('creator', 'Content Creator'), ('admin', 'Admin member')], max_length=255),
        ),
    ]
