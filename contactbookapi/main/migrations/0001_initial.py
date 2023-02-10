# Generated by Django 4.1.6 on 2023-02-08 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.CharField(max_length=4)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('work_phone', models.CharField(max_length=12)),
                ('personal_phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=100)),
                ('birthday', models.CharField(max_length=50)),
            ],
        ),
    ]