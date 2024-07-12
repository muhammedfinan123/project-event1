# Generated by Django 5.0.6 on 2024-05-27 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pic')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]
