# Generated by Django 2.1 on 2018-09-05 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=25)),
                ('time', models.CharField(max_length=13)),
                ('amount', models.IntegerField()),
                ('account', models.CharField(max_length=255)),
                ('create_time', models.BigIntegerField(blank=True, default=0)),
                ('perform_time', models.BigIntegerField(blank=True, default=0)),
                ('cancel_time', models.BigIntegerField(blank=True, default=0)),
                ('transaction', models.CharField(max_length=25)),
                ('state', models.SmallIntegerField()),
                ('reason', models.SmallIntegerField(blank=True, default=0)),
                ('receivers', models.CharField(max_length=500)),
                ('order_id', models.IntegerField()),
            ],
        ),
    ]
