# Generated by Django 3.2.9 on 2024-09-23 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routineexercise',
            name='routine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routineexercise_set', to='api.routine'),
        ),
    ]
