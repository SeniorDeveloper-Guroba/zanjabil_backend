# Generated by Django 4.0.5 on 2022-07-31 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zanjabil_backend', '0007_alter_menu_options_alter_menucategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucategory',
            name='icon',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='menucategory',
            name='name',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
