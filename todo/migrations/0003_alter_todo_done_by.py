# Generated by Django 3.2 on 2023-02-21 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_executionrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='done_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='done_by', to=settings.AUTH_USER_MODEL),
        ),
    ]