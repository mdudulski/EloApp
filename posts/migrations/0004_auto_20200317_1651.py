# Generated by Django 3.0.4 on 2020-03-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(choices=[('Adam', 'Adam'), ('Bartek', 'Bartek'), ('Paweł', 'Paweł'), ('Mateusz', 'Mateusz')], max_length=100),
        ),
    ]
