# Generated by Django 3.2.3 on 2021-12-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=17, null=True, unique=True, verbose_name='Mobile Number'),
        ),
    ]
