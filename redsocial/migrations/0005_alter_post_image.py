# Generated by Django 4.1 on 2022-09-02 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redsocial', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
    ]
