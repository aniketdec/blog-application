# Generated by Django 2.0.8 on 2019-07-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20190718_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='follow', to='users.Profile'),
        ),
    ]
