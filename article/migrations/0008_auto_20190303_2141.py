# Generated by Django 2.1.7 on 2019-03-03 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]
