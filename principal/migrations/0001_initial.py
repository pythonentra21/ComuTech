# Generated by Django 3.2.7 on 2021-09-14 17:59

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('cpf', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)])),
                ('telefone', models.CharField(max_length=13)),
                ('cep', models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(8)])),
                ('data_nascimento', models.DateTimeField()),
                ('senha', models.CharField(max_length=255)),
                ('whatsapp', models.CharField(max_length=13)),
                ('twitter', models.CharField(blank=True, max_length=15, validators=[django.core.validators.MinLengthValidator(4)])),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('instagram', models.CharField(blank=True, max_length=30)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
