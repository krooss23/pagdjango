# Generated by Django 4.1.2 on 2023-06-13 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airsoftcqb', '0002_rename_correoelectrico_player_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='airsoftcqb.estado', verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='player',
            name='nombreTeam',
            field=models.CharField(max_length=50, verbose_name='Nombre Team'),
        ),
    ]