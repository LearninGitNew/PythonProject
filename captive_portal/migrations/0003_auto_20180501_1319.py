# Generated by Django 2.0.4 on 2018-05-01 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('captive_portal', '0002_auto_20180501_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wifiuser',
            name='qr_code',
            field=models.FileField(upload_to='C:\\Users\\Vezral\\PycharmProjects\\PythonCaptivePortal\\media'),
        ),
    ]
