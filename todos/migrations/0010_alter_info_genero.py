# Generated by Django 4.2.7 on 2023-11-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0009_alter_info_genero"),
    ]

    operations = [
        migrations.AlterField(
            model_name="info",
            name="genero",
            field=models.CharField(
                choices=[("Macho", "Macho"), ("Fêmea", "Fêmea")],
                max_length=10,
                null=True,
                verbose_name="Genero",
            ),
        ),
    ]
