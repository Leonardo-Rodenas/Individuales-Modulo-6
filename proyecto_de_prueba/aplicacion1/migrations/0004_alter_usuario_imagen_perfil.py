# Generated by Django 4.2.1 on 2023-06-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0003_alter_usuario_imagen_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='aplicacion1/static/img/perfil/'),
        ),
    ]
