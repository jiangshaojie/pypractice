# Generated by Django 3.0.1 on 2019-12-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
