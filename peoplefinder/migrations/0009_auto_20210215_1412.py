# Generated by Django 3.1.6 on 2021-02-15 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoplefinder', '0008_auto_20210215_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='head_of_team',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teammember',
            name='job_title',
            field=models.CharField(default='Tester', max_length=100),
            preserve_default=False,
        ),
    ]
