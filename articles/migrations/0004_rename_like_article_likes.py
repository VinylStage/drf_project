# Generated by Django 4.2 on 2023-04-24 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_like_alter_comment_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='like',
            new_name='likes',
        ),
    ]
