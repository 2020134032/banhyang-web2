# Generated by Django 3.0.4 on 2020-05-25 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingTitle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AccountingDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('value', models.IntegerField()),
                ('note', models.TextField()),
                ('remark', models.TextField(null=True)),
                ('accounting_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AccountingTitle')),
            ],
        ),
    ]
