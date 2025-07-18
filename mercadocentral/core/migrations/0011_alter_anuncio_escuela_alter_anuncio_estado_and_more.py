# Generated by Django 5.2.1 on 2025-06-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_anuncio_talla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='escuela',
            field=models.CharField(blank=True, choices=[('ESC_NIN', 'Ninguna'), ('ESC_CHI', 'Hispano Inglés')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='estado',
            field=models.CharField(blank=True, choices=[('EST_ALL', 'No precisado'), ('EST_NUEVO', 'Nuevo'), ('EST_COMNUE', 'Como nuevo'), ('EST_PRIM', 'Primera mano'), ('EST_SEC', 'Secunda mano')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='genero',
            field=models.CharField(blank=True, choices=[('GEN_ALL', 'Todos'), ('GEN_MX', 'Mixto'), ('GEN_NO', 'Niño'), ('GEN_NA', 'Niña')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='materia',
            field=models.CharField(blank=True, choices=[('MAT_ALL', 'Todos'), ('MAT_MZ', 'Mezcla'), ('MAT_AG', '100% Algodon o Lana'), ('MAT_SY', '100% Syntetico')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='prenda',
            field=models.CharField(choices=[('PRD_ALL', 'Lote'), ('PRD_POL', 'Polo'), ('PRD_JER', 'Jersey'), ('PRD_FAL', 'Falda'), ('PRD_PAN', 'Pantalón'), ('PRD_CHD', 'Chandal'), ('PRD_BER', 'Bermuda'), ('PRD_BAB', 'Babi')], default='PRD_ALL', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='talla',
            field=models.CharField(choices=[('74', '00'), ('78', '0'), ('82', '1'), ('98', '2'), ('108', '4'), ('118', '6'), ('128', '8'), ('140', '10'), ('152', '12'), ('164', '14'), ('170', '16 / S / 2A'), ('178', '18 / M / 3A'), ('184', '20 / L / 4A'), ('188', '22 / XL / 5A'), ('192', '24 / XXL / 6A')], default='74', max_length=64),
            preserve_default=False,
        ),
    ]
