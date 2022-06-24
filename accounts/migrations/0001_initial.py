# Generated by Django 3.2 on 2022-06-21 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(default='operational', max_length=50)),
                ('status', models.IntegerField()),
                ('verified', models.BooleanField(db_index=True, default=False)),
            ],
        ),
    ]
