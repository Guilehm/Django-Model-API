# Generated by Django 2.0.4 on 2018-04-10 14:01

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180410_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', '32'), ('2', '34'), ('3', '36'), ('4', '40'), ('5', '44'), ('6', '46'), ('7', '48')], default='1', max_length=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('1', 'Terno'), ('2', 'Calça'), ('3', 'Camisa')], max_length=7),
        ),
    ]
