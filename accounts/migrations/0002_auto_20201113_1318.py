# Generated by Django 3.1.3 on 2020-11-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='DOB',
            field=models.DateField(blank=True, max_length=8, null=True),
        ),
    ]
