# Generated by Django 4.0.5 on 2022-07-31 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zanjabil_backend', '0010_remove_menu_category_remove_menucategory_dishes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='menu',
            new_name='menu_id',
        ),
    ]
