# Generated by Django 3.1.4 on 2021-10-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_loyal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=500)),
                ('Img', models.ImageField(upload_to='media')),
                ('Valid', models.DateField()),
            ],
        ),
    ]