# Generated by Django 4.0.6 on 2022-07-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
