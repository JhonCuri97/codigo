# Generated by Django 3.2.11 on 2022-01-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
