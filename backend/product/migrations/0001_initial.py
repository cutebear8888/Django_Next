# Generated by Django 5.1.2 on 2024-11-06 23:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_explanation', models.TextField()),
            ],
        ),
    ]