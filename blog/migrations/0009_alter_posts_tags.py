# Generated by Django 3.2.6 on 2023-09-04 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20230904_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_tags', to='blog.tags'),
        ),
    ]
