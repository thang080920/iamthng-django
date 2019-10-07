# Generated by Django 2.2.6 on 2019-10-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Search',
                'verbose_name_plural': 'Searchs',
                'db_table': '',
                'managed': True,
            },
        ),
    ]