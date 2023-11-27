# Generated by Django 4.2.7 on 2023-11-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0006_remove_info_pet_info_breed_info_color_info_genero_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="info",
            name="genero",
            field=models.CharField(
                choices=[("M", "Macho"), ("F", "Fêmea")],
                max_length=20,
                null=True,
                verbose_name="Genero",
            ),
        ),
    ]