# Generated by Django 5.1.3 on 2024-11-29 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('B', 'Basico'), ('I', 'Intermediario'), ('A', 'Avancado')], default='B', max_length=1),
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.aluno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.curso')),
            ],
        ),
    ]
