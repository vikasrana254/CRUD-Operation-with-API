# Generated by Django 3.2 on 2021-08-05 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=41),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=12),
        ),
    ]
