# Generated by Django 2.2 on 2019-08-13 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims', '0005_auto_20190813_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultfields',
            old_name='created_by',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='resultfields',
            old_name='updated_by',
            new_name='updated',
        ),
        migrations.AlterField(
            model_name='client',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 13, 22, 55, 48, 324888)),
        ),
        migrations.AlterField(
            model_name='field',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 13, 22, 55, 48, 323888)),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 13, 22, 55, 48, 328873)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 13, 22, 55, 48, 327874)),
        ),
        migrations.AlterField(
            model_name='resultfields',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 13, 22, 55, 48, 326902)),
        ),
        migrations.AlterField(
            model_name='sample',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 13, 22, 55, 48, 325906)),
        ),
        migrations.AlterField(
            model_name='sampletest',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 13, 22, 55, 48, 325906)),
        ),
        migrations.AlterField(
            model_name='section',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 13, 22, 55, 48, 321890)),
        ),
        migrations.AlterField(
            model_name='test',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 13, 22, 55, 48, 322894)),
        ),
    ]
