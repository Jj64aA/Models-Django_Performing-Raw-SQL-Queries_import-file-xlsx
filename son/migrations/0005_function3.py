# Generated by Django 4.1.7 on 2023-07-03 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('son', '0004_function2'),
    ]

    operations = [
        migrations.CreateModel(
            name='function3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_code_f2', models.CharField(max_length=3)),
                ('Nb_Fact_all', models.IntegerField()),
                ('Nb', models.IntegerField()),
                ('montant_f3', models.FloatField()),
            ],
        ),
    ]
