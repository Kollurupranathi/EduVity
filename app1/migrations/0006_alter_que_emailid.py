# Generated by Django 4.1.2 on 2022-11-05 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_name_que_firstname_que_confirmpassword_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='que',
            name='emailId',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
