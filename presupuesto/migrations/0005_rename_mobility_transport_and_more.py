# Generated by Django 4.0.3 on 2022-04-21 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0004_project_bop_cost_project_construction_cost_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mobility',
            new_name='Transport',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='mobility_cost',
            new_name='transport_cost',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='transport',
            new_name='vehicule',
        ),
    ]
