# Generated by Django 4.2.6 on 2023-11-15 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_rename_images_employee_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
