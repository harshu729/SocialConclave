# Generated by Django 3.1.3 on 2021-03-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20210305_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegate',
            name='topicPref2',
            field=models.CharField(choices=[(0, 'CLIMATE ACTION'), (1, 'FINANCIAL INDEPENDENCE OF WOMEN'), (2, 'RURAL ILLITERACY AND UNEMPLOYMENT'), (3, 'YOUTH PRIVACY AND SOCIAL MEDIA'), (4, 'ZERO HUNGER')], default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='topicPref3',
            field=models.CharField(choices=[(0, 'CLIMATE ACTION'), (1, 'FINANCIAL INDEPENDENCE OF WOMEN'), (2, 'RURAL ILLITERACY AND UNEMPLOYMENT'), (3, 'YOUTH PRIVACY AND SOCIAL MEDIA'), (4, 'ZERO HUNGER')], default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='topicPref4',
            field=models.CharField(choices=[(0, 'CLIMATE ACTION'), (1, 'FINANCIAL INDEPENDENCE OF WOMEN'), (2, 'RURAL ILLITERACY AND UNEMPLOYMENT'), (3, 'YOUTH PRIVACY AND SOCIAL MEDIA'), (4, 'ZERO HUNGER')], default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='topicPref5',
            field=models.CharField(choices=[(0, 'CLIMATE ACTION'), (1, 'FINANCIAL INDEPENDENCE OF WOMEN'), (2, 'RURAL ILLITERACY AND UNEMPLOYMENT'), (3, 'YOUTH PRIVACY AND SOCIAL MEDIA'), (4, 'ZERO HUNGER')], default=None, max_length=2000),
        ),
    ]
