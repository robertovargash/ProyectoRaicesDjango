# Generated by Django 4.1 on 2022-08-29 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valeitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=6, max_digits=18)),
                ('precio', models.DecimalField(decimal_places=6, max_digits=18)),
                ('mercancia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.mercancia')),
                ('vale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.vale')),
            ],
        ),
    ]
