# Generated by Django 3.2.6 on 2021-09-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='dis',
            field=models.TextField(blank=True, null=True),
        ),
    ]