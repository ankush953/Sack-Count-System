# Generated by Django 2.1.7 on 2019-07-18 04:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=20)),
                ('middlename', models.CharField(blank=True, max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('Email_address', models.EmailField(max_length=254, unique=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile_pic/default-user.jpg', upload_to=users.models.imagepath)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]