# Generated by Django 4.2.7 on 2023-11-21 12:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0002_alter_todo_deadline_alter_todo_finished_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="todo",
            options={"ordering": ["deadline"]},
        ),
        migrations.AddField(
            model_name="todo",
            name="breed",
            field=models.CharField(
                max_length=100, null=True, verbose_name="Tipo de Pet"
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="deadline",
            field=models.DateField(verbose_name="Data de Retirada"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Nome do Pet"),
        ),
    ]
