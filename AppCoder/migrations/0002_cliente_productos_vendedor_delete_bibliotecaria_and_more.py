# Generated by Django 5.1.3 on 2024-11-24 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_de_pedido', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Turno', models.CharField(max_length=40)),
                ('Monto_caja', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bibliotecaria',
        ),
        migrations.DeleteModel(
            name='Lector',
        ),
        migrations.DeleteModel(
            name='Libro',
        ),
    ]
