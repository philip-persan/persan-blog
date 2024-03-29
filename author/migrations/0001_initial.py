# Generated by Django 4.1.4 on 2022-12-26 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profissao', models.CharField(default='Desenvolvedor', max_length=100, verbose_name='Profissão')),
                ('nivel', models.CharField(choices=[('JR', 'Junior'), ('PL', 'Pleno'), ('SR', 'Seinor')], default='JR', max_length=20, verbose_name='Nível')),
                ('sexo', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Non Binary')], default='M', max_length=1, verbose_name='Sexo')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Aniversário')),
                ('pais', models.CharField(blank=True, max_length=100, null=True, verbose_name='País')),
                ('estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
    ]
