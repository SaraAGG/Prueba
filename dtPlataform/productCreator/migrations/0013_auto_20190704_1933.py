# Generated by Django 2.2.3 on 2019-07-04 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productCreator', '0012_auto_20190704_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='attribute_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='attribute_ref_id', to='productCreator.Attributess'),
        ),
    ]
