# Generated by Django 2.2.7 on 2019-11-23 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20191123_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfor',
            name='dateHired',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='email',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='phoneNumber',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='position',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='salary',
            field=models.CharField(max_length=64),
        ),
    ]
