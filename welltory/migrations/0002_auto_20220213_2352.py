# Generated by Django 3.2 on 2022-02-13 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welltory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biomarker',
            name='description',
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='disease',
        ),
        migrations.AlterField(
            model_name='biomarker',
            name='bio_marker',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='biomarker',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
