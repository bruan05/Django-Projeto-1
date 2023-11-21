# Generated by Django 4.2.7 on 2023-11-21 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0003_alter_todo_options_todo_breed_alter_todo_deadline_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="color",
            field=models.CharField(
                max_length=100, null=True, verbose_name="Cor do Pet"
            ),
        ),
        migrations.AddField(
            model_name="todo",
            name="genero",
            field=models.CharField(max_length=100, null=True, verbose_name="Genero"),
        ),
        migrations.AddField(
            model_name="todo",
            name="tipe",
            field=models.CharField(
                max_length=100, null=True, verbose_name="Tipo de Pet"
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="breed",
            field=models.CharField(
                max_length=100, null=True, verbose_name="Raça do Pet"
            ),
        ),
    ]
