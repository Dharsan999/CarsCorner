# Generated by Django 2.2 on 2022-07-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Owner', '0005_auto_20210207_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='Owner_license',
            field=models.ImageField(upload_to='img/Owner_License/Driving_License.jpg'),
        ),
    ]
