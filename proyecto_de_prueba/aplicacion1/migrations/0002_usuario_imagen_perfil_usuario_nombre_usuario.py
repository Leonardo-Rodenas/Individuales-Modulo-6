# Generated by Django 4.2.1 on 2023-06-06 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='perfil/'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre_usuario',
            field=models.CharField(default='usuario', max_length=100, unique=True),
        ),
    ]
