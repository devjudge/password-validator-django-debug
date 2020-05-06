# Generated by Django 2.1 on 2020-05-06 09:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    def insertData(apps, schema_editor):
        Login = apps.get_model('restapi', 'Users_Details')
        user = Login(name="admin", email="abc@gmail.com", password="abcd123456")
        user.save()

    operations = [
        migrations.CreateModel(
            name='Users_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('confirm_password', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
            ],
        ),
        migrations.RunPython(insertData)
    ]