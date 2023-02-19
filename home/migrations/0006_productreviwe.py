# Generated by Django 4.1.5 on 2023-02-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReviwe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('star', models.IntegerField()),
                ('comment', models.TextField()),
                ('slug', models.CharField(max_length=500)),
            ],
        ),
    ]
