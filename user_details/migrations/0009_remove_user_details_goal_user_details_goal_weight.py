# Generated by Django 4.1.3 on 2022-12-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0008_alter_user_details_height'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='goal',
        ),
        migrations.AddField(
            model_name='user_details',
            name='goal_weight',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
