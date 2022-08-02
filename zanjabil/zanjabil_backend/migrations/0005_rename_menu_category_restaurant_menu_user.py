# Generated by Django 4.0.5 on 2022-07-26 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zanjabil_backend', '0004_alter_dish_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='menu_category',
            new_name='menu',
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zanjabil_backend.address')),
            ],
        ),
    ]
