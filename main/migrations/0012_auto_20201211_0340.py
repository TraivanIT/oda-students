# Generated by Django 3.0.2 on 2020-12-11 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201211_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='finishWithODA',
            field=models.DateField(null=True),
        ),
    ]
