# Generated by Django 3.1.6 on 2021-02-09 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peoplefinder', '0002_auto_20210209_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='TeamTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='peoplefinder.team')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='peoplefinder.team')),
            ],
            options={
                'unique_together': {('parent', 'child')},
            },
        ),
    ]