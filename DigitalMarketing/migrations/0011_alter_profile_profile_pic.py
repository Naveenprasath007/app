# Generated by Django 4.1.7 on 2023-11-15 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalMarketing', '0010_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='\\media\\Profile\\Default.jpg', null=True, upload_to=''),
        ),
    ]