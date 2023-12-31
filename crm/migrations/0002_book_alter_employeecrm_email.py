# Generated by Django 4.1 on 2023-10-31 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=100)),
                ('authorname', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='employeecrm',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
