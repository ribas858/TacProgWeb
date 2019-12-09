# Generated by Django 2.2.7 on 2019-11-21 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitecampus', '0004_auto_20191121_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='estado',
            field=models.CharField(choices=[('1', 'Rascunho'), ('2', 'Em Revisão'), ('3', 'Pronto')], default='', max_length=1),
        ),
        migrations.AddField(
            model_name='post',
            name='semestrepub',
            field=models.CharField(choices=[('1', '2019/1'), ('2', '2018/2'), ('3', '2018/1'), ('4', '2017/2')], default='', max_length=1),
        ),
    ]