# Generated by Django 4.1.5 on 2023-02-01 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('post', models.CharField(max_length=500)),
                ('comment', models.TextField()),
                ('star', models.IntegerField()),
            ],
        ),
    ]
