# Generated by Django 2.2.6 on 2019-10-10 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=200)),
                ('active', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'todo',
                'verbose_name_plural': 'todos',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
