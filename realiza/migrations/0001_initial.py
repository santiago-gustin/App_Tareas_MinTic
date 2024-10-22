# Generated by Django 5.1.2 on 2024-10-22 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realiza',
            fields=[
                ('id_realiza', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'realiza',
                'managed': False,
            },
        ),
    ]
