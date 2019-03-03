# Generated by Django 2.1.7 on 2019-03-03 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20190303_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='İsim')),
                ('comment_content', models.CharField(max_length=200, verbose_name='Yorum')),
                ('comment_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article', verbose_name='Makale')),
            ],
        ),
    ]
