# Generated by Django 4.0 on 2022-01-09 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_messagemodel_receiver_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagemodel',
            old_name='sender_user',
            new_name='user1',
        ),
        migrations.RenameField(
            model_name='messagemodel',
            old_name='receiver_user',
            new_name='user2',
        ),
        migrations.RenameField(
            model_name='threadmodel',
            old_name='user',
            new_name='user1',
        ),
        migrations.RenameField(
            model_name='threadmodel',
            old_name='receiver',
            new_name='user2',
        ),
    ]
