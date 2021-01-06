# Generated by Django 2.2.3 on 2019-07-04 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productCreator', '0002_auto_20190704_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='product_ref_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_ref_id', to='productCreator.Productss'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_ref_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_ref_id', to='productCreator.Attributess'),
        ),
    ]
