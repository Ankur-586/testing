# Generated by Django 4.1.2 on 2022-11-30 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0005_remove_student_subject_delete_combined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subject',
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='StudentApp.subject'),
        ),
    ]
