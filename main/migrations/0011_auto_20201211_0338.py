# Generated by Django 3.0.2 on 2020-12-11 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_classes_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='finishWithODA',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='haveJob',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='jobDescription',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='jobName',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='student',
            name='studentFeedback',
            field=models.TextField(blank=True),
        ),
    ]
