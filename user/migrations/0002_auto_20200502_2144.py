# Generated by Django 3.0.5 on 2020-05-02 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbilling',
            name='house_nr',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userbilling',
            name='postal_code',
            field=models.IntegerField(),
        ),
    ]