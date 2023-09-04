# Generated by Django 3.2.6 on 2023-09-04 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_posts_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AlterField(
            model_name='posts',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.comment', verbose_name='Post_Comments'),
        ),
    ]
