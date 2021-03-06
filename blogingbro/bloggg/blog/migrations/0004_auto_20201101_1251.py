# Generated by Django 3.1b1 on 2020-11-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='contact',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='person',
            name='postalcode',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=20),
        ),
    ]
