# Generated by Django 4.2 on 2023-04-17 20:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.JSONField()),
                ('name', models.CharField(max_length=255)),
                ('weight', models.JSONField()),
                ('height', models.JSONField()),
                ('life_span', models.CharField(max_length=255)),
                ('origin', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'dogs',
            },
        ),
        migrations.CreateModel(
            name='DogTemperament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='breed.dog')),
            ],
            options={
                'db_table': 'dog_temperament',
            },
        ),
        migrations.CreateModel(
            name='Temperament',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('dogs', models.ManyToManyField(related_name='dog_temperament', through='breed.DogTemperament', to='breed.dog')),
            ],
            options={
                'db_table': 'temperaments',
            },
        ),
        migrations.AddField(
            model_name='dogtemperament',
            name='temperament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='breed.temperament'),
        ),
        migrations.AddField(
            model_name='dog',
            name='temperaments',
            field=models.ManyToManyField(related_name='dog_temperament', through='breed.DogTemperament', to='breed.temperament'),
        ),
    ]
