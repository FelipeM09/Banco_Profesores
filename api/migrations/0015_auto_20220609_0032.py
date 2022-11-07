# Generated by Django 3.2.3 on 2022-06-09 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_usuarios_genero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivos',
            name='ruta',
        ),
        migrations.AddField(
            model_name='archivos',
            name='date_time_upload',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='archivos',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
