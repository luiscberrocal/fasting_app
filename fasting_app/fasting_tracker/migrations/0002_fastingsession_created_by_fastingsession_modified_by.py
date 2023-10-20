# Generated by Django 4.2.6 on 2023-10-20 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("fasting_tracker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="fastingsession",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created_%(class)s",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="fastingsession",
            name="modified_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="modified_%(class)s",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]