# Generated by Django 4.0.5 on 2022-08-04 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_options_post_date_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]