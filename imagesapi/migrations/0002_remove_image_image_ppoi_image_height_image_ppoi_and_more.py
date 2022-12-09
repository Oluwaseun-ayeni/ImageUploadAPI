# Generated by Django 4.1.3 on 2022-12-09 19:00

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('imagesapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_ppoi',
        ),
        migrations.AddField(
            model_name='image',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Height'),
        ),
        migrations.AddField(
            model_name='image',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI'),
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Width'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(height_field='height', upload_to='pictures/', verbose_name='image', width_field='width'),
        ),
    ]
