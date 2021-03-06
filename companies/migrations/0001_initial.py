# Generated by Django 2.1.7 on 2019-07-18 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='')),
                ('establishment_year', models.DateField()),
                ('contract_date_time', models.DateTimeField()),
                ('contract_duration', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('number_of_trucks', models.IntegerField()),
            ],
        ),
    ]
