# Generated by Django 2.0.5 on 2018-05-06 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0003_images_location_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='display.Tag'),
        ),
        migrations.AddField(
            model_name='images',
            name='time_posted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]