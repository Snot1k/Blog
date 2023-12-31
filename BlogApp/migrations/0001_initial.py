# Generated by Django 4.2.3 on 2023-09-23 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_header', models.CharField(max_length=50)),
                ('post_text', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField()),
                ('category', models.ForeignKey(default='no category', on_delete=django.db.models.deletion.SET_DEFAULT, to='BlogApp.category')),
            ],
        ),
    ]
