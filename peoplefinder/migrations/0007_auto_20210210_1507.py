# Generated by Django 3.1.6 on 2021-02-10 15:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoplefinder', '0006_auto_20210209_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='abbreviation',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='people',
            field=models.ManyToManyField(related_name='teams', through='peoplefinder.TeamMember', to=settings.AUTH_USER_MODEL),
        ),
    ]