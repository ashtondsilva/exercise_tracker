# Generated by Django 3.2.9 on 2024-09-20 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20240920_0556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routineexercise',
            name='exercise',
        ),
        migrations.AddField(
            model_name='routineexercise',
            name='exercise_type',
            field=models.CharField(choices=[('Strength', 'Strength'), ('Cardio', 'Cardio'), ('Flexibility', 'Flexibility'), ('Balance', 'Balance'), ('Plyometric', 'Plyometric'), ('Bodyweight', 'Bodyweight')], default='Strength', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='routineexercise',
            name='routine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='api.routine'),
        ),
    ]
