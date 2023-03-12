# Generated by Django 4.1.7 on 2023-03-12 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SitioWeb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orden',
            old_name='dato_agred',
            new_name='date_create',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='orden',
            name='transaccion_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, default=0, null=True)),
                ('dato_agred', models.DateTimeField(auto_now_add=True)),
                ('orden', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SitioWeb.orden')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SitioWeb.producto')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SitioWeb.usuario'),
        ),
    ]
