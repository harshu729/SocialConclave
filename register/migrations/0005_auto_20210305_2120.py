# Generated by Django 3.1.3 on 2021-03-05 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20210305_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegate',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=200),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='topicPref1',
            field=models.CharField(choices=[('CLIMATE ACTION', 'CLIMATE ACTION'), ('FINANCIAL INDEPENDENCE OF WOMEN', 'FINANCIAL INDEPENDENCE OF WOMEN'), ('RURAL ILLITERACY AND UNEMPLOYMENT', 'RURAL ILLITERACY AND UNEMPLOYMENT'), ('YOUTH PRIVACY AND SOCIAL MEDIA', 'YOUTH PRIVACY AND SOCIAL MEDIA'), ('ZERO HUNGER', 'ZERO HUNGER')], default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='topicPref2',
            field=models.CharField(choices=[('CLIMATE ACTION', 'CLIMATE ACTION'), ('FINANCIAL INDEPENDENCE OF WOMEN', 'FINANCIAL INDEPENDENCE OF WOMEN'), ('RURAL ILLITERACY AND UNEMPLOYMENT', 'RURAL ILLITERACY AND UNEMPLOYMENT'), ('YOUTH PRIVACY AND SOCIAL MEDIA', 'YOUTH PRIVACY AND SOCIAL MEDIA'), ('ZERO HUNGER', 'ZERO HUNGER')], default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='topicPref3',
            field=models.CharField(choices=[('CLIMATE ACTION', 'CLIMATE ACTION'), ('FINANCIAL INDEPENDENCE OF WOMEN', 'FINANCIAL INDEPENDENCE OF WOMEN'), ('RURAL ILLITERACY AND UNEMPLOYMENT', 'RURAL ILLITERACY AND UNEMPLOYMENT'), ('YOUTH PRIVACY AND SOCIAL MEDIA', 'YOUTH PRIVACY AND SOCIAL MEDIA'), ('ZERO HUNGER', 'ZERO HUNGER')], default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='topicPref4',
            field=models.CharField(choices=[('CLIMATE ACTION', 'CLIMATE ACTION'), ('FINANCIAL INDEPENDENCE OF WOMEN', 'FINANCIAL INDEPENDENCE OF WOMEN'), ('RURAL ILLITERACY AND UNEMPLOYMENT', 'RURAL ILLITERACY AND UNEMPLOYMENT'), ('YOUTH PRIVACY AND SOCIAL MEDIA', 'YOUTH PRIVACY AND SOCIAL MEDIA'), ('ZERO HUNGER', 'ZERO HUNGER')], default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='topicPref5',
            field=models.CharField(choices=[('CLIMATE ACTION', 'CLIMATE ACTION'), ('FINANCIAL INDEPENDENCE OF WOMEN', 'FINANCIAL INDEPENDENCE OF WOMEN'), ('RURAL ILLITERACY AND UNEMPLOYMENT', 'RURAL ILLITERACY AND UNEMPLOYMENT'), ('YOUTH PRIVACY AND SOCIAL MEDIA', 'YOUTH PRIVACY AND SOCIAL MEDIA'), ('ZERO HUNGER', 'ZERO HUNGER')], default=None, max_length=2000),
        ),
    ]
