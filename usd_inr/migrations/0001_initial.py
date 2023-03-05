# Generated by Django 4.1.7 on 2023-03-04 14:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GdpData',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('e2e4bafd-955b-4847-a471-05f899bb1352'), editable=False, primary_key=True, serialize=False)),
                ('create_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('usd_data', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=16, null=True)),
            ],
        ),
    ]
