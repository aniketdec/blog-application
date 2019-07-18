# Generated by Django 2.0.8 on 2019-07-13 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_profile_about_me'),
        ('blog', '0013_remove_post_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='avatar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]