# Generated by Django 3.1.4 on 2021-01-12 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='NAME')),
            ],
            options={
                'db_table': 'DIAGNOSIS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='NAME')),
                ('surname', models.TextField(db_column='SURNAME')),
                ('department', models.TextField(db_column='DEPARTMENT')),
                ('title', models.TextField(blank=True, db_column='TITLE', null=True)),
                ('email', models.TextField(blank=True, db_column='EMAIL', null=True)),
                ('phone', models.TextField(blank=True, db_column='PHONE', null=True)),
                ('salary', models.TextField(blank=True, db_column='SALARY', null=True)),
                ('off_day', models.TextField(blank=True, db_column='OFF_DAY', null=True)),
            ],
            options={
                'db_table': 'DOCTOR',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='NAME')),
                ('surname', models.TextField(db_column='SURNAME')),
                ('gender', models.TextField(blank=True, db_column='GENDER', null=True)),
                ('birthdate', models.DateField(blank=True, db_column='BIRTHDATE', null=True)),
                ('email', models.TextField(blank=True, db_column='EMAIL', null=True)),
                ('phone', models.TextField(blank=True, db_column='PHONE', null=True)),
            ],
            options={
                'db_table': 'PATIENT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='NAME')),
                ('unit_price', models.TextField(db_column='UNIT_PRICE')),
                ('quantity', models.IntegerField(db_column='QUANTITY')),
            ],
            options={
                'db_table': 'SERVICE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('type', models.TextField(db_column='TYPE')),
                ('date', models.DateField(blank=True, db_column='DATE', null=True)),
                ('state', models.IntegerField(db_column='STATE')),
            ],
            options={
                'db_table': 'VISIT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VisitProcess',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('process_date', models.DateField(blank=True, db_column='PROCESS_DATE', null=True)),
            ],
            options={
                'db_table': 'VISIT_PROCESS',
                'managed': False,
            },
        ),
    ]
