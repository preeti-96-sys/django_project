# Generated by Django 3.1.4 on 2021-10-11 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loyal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Contact', models.CharField(max_length=14)),
                ('Email', models.CharField(max_length=50)),
                ('Last', models.DateField(auto_now=True)),
            ],
        ),
    ]