# Generated by Django 2.1.7 on 2019-02-20 13:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sls_dt', models.DateField(default=datetime.datetime.now, verbose_name='日付')),
                ('prc_amt', models.IntegerField(help_text='単位は日本円', verbose_name='金額')),
                ('memo', models.CharField(max_length=500, verbose_name='メモ')),
            ],
            options={
                'db_table': 'AccountBook',
            },
        ),
        migrations.CreateModel(
            name='ExpnsCatg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expns_catg_nm', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'ExpnsCatg',
            },
        ),
        migrations.AddField(
            model_name='accountbook',
            name='expns_catg_nm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accountbook.ExpnsCatg', verbose_name='カテゴリ'),
        ),
    ]