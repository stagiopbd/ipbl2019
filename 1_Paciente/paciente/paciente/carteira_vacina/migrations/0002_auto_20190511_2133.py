# Generated by Django 2.0.2 on 2019-05-11 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carteira_vacina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('med_id', models.AutoField(primary_key=True, serialize=False)),
                ('med_active_principle', models.CharField(max_length=150)),
                ('med_code_ggrem', models.CharField(max_length=15)),
                ('med_register', models.CharField(max_length=13)),
                ('med_ean1', models.CharField(max_length=14)),
                ('med_ean2', models.CharField(max_length=14)),
                ('med_ean3', models.CharField(max_length=14)),
                ('med_product_description', models.CharField(max_length=120)),
                ('med_presentation', models.CharField(max_length=200)),
                ('med_hospital_restrictions', models.BooleanField()),
                ('med_cap', models.BooleanField()),
                ('med_confaz87', models.BooleanField()),
                ('med_marketing_year', models.IntegerField()),
                ('med_sup_id', models.IntegerField()),
                ('med_thc_id', models.IntegerField()),
                ('med_pdt_id', models.IntegerField()),
                ('med_stp_id', models.IntegerField()),
            ],
            options={
                'db_table': 'medicine',
            },
        ),
        migrations.RemoveField(
            model_name='carteiravacina',
            name='vac_name',
        ),
        migrations.AlterField(
            model_name='carteiravacina',
            name='vac_cpfpatient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.Paciente'),
        ),
        migrations.AlterModelTable(
            name='carteiravacina',
            table='vaccination',
        ),
        migrations.AddField(
            model_name='carteiravacina',
            name='vac_medicine',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='carteira_vacina.Medicamento'),
            preserve_default=False,
        ),
    ]
