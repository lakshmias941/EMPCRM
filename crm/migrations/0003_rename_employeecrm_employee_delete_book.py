# Generated by Django 4.1 on 2023-11-02 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_book_alter_employeecrm_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='employeecrm',
            new_name='Employee',
        ),
        migrations.DeleteModel(
            name='book',
        ),
    ]