# Generated by Django 4.1 on 2022-08-26 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('almacen', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Clasificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clasificacion', models.CharField(max_length=30)),
                ('detalles', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Mercancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nombremercancia', models.CharField(max_length=1000)),
                ('descripcion', models.CharField(max_length=1000)),
                ('um', models.CharField(max_length=50)),
                ('clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.clasificaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('observaciones', models.CharField(default='', max_length=250)),
                ('precibe', models.CharField(default='', max_length=250)),
                ('pentrega', models.CharField(default='', max_length=250)),
                ('pautoriza', models.CharField(default='', max_length=250)),
                ('contrato', models.CharField(default='', max_length=50)),
                ('factura', models.CharField(default='', max_length=50)),
                ('conduce', models.CharField(default='', max_length=50)),
                ('scompra', models.CharField(default='', max_length=50)),
                ('manifiesto', models.CharField(default='', max_length=50)),
                ('partida', models.CharField(default='', max_length=50)),
                ('conocimiento', models.CharField(default='', max_length=50)),
                ('expedicion', models.CharField(default='', max_length=50)),
                ('casilla', models.CharField(default='', max_length=50)),
                ('bultos', models.CharField(default='', max_length=50)),
                ('tbultos', models.CharField(default='', max_length=50)),
                ('transportista', models.CharField(default='', max_length=250)),
                ('tci', models.CharField(default='', max_length=11)),
                ('tchapa', models.CharField(default='', max_length=50)),
                ('proveedor', models.CharField(default='', max_length=250)),
                ('fecha', models.DateField()),
                ('activo', models.IntegerField(default=0)),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.almacen')),
            ],
        ),
        migrations.CreateModel(
            name='Vale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('observaciones', models.CharField(default='', max_length=250)),
                ('psolicita', models.CharField(default='', max_length=250)),
                ('pentrega', models.CharField(default='', max_length=250)),
                ('pautoriza', models.CharField(default='', max_length=250)),
                ('fecha', models.DateField()),
                ('activo', models.IntegerField(default=0)),
                ('tipovale', models.IntegerField()),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.almacen')),
            ],
        ),
        migrations.CreateModel(
            name='Recepcionmercancias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=6, max_digits=18)),
                ('precio', models.DecimalField(decimal_places=6, max_digits=18)),
                ('mercancia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.mercancia')),
                ('recepcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.recepcion')),
            ],
        ),
        migrations.CreateModel(
            name='Almacenmercancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=6, max_digits=18)),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.almacen')),
                ('mercancia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.mercancia')),
            ],
        ),
    ]
