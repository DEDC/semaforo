# Generated by Django 2.2.4 on 2019-09-05 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0003_auto_20190829_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evidencias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidencia', models.FileField(blank=True, null=True, upload_to='evidencias/')),
                ('nombre', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evidencias', to='direccion.Actividades')),
            ],
        ),
    ]
