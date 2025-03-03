# Generated by Django 4.1.13 on 2025-03-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('subcategory', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('amount', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('unavailable', 'Unavailable'), ('available', 'Available')], default='unavailable', max_length=15)),
            ],
        ),
    ]
