# Generated by Django 2.2 on 2022-07-23 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Owner', '0006_auto_20220723_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='Owner_license',
            field=models.ImageField(upload_to='img/Owner_License/'),
        ),
    ]
