# Generated by Django 4.0.6 on 2022-08-20 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.TextField()),
                ('score', models.TextField()),
                ('category', models.TextField()),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('like1', models.CharField(max_length=10)),
                ('like2', models.CharField(max_length=10)),
                ('like3', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('foodname', models.TextField()),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'menu',
            },
        ),
    ]
