# Generated by Django 2.2.5 on 2019-10-03 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts_demand', '0003_auto_20191003_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partsdemand',
            name='status',
            field=models.CharField(choices=[('Finalizado', 'Finalizado'), ('Não Finalizado', 'Não Finalizado')], max_length=500),
        ),
    ]