from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='anio',
            field=models.PositiveIntegerField(verbose_name='año'),
        ),
    ]
