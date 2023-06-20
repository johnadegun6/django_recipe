# Generated by Django 4.2.1 on 2023-06-20 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('directions', models.TextField()),
                ('servings', models.CharField(max_length=5)),
                ('timee', models.CharField(max_length=5)),
                ('calories', models.CharField(max_length=5)),
                ('fat', models.CharField(max_length=5)),
                ('carbs', models.CharField(max_length=5)),
                ('protein', models.CharField(max_length=5)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.topic')),
            ],
        ),
    ]