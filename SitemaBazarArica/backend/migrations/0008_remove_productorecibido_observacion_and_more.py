# Generated by Django 4.2.4 on 2023-12-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_pedido_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productorecibido',
            name='observacion',
        ),
        migrations.AddField(
            model_name='pedido',
            name='observacion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
