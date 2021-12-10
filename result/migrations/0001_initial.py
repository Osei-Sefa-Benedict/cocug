# Generated by Django 3.2.9 on 2021-12-10 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=45)),
                ('subject_code', models.IntegerField(unique=True)),
                ('marks', models.IntegerField()),
                ('pass_mark', models.IntegerField()),
                ('add_date', models.DateField(auto_now_add=True)),
                ('select_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.classregistration')),
            ],
        ),
    ]
