# Generated by Django 3.2.6 on 2022-03-19 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tutores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField(auto_now_add=True)),
                ('tutor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tutores.tutor')),
            ],
        ),
    ]
