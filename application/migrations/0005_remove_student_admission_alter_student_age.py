# Generated by Django 5.1.3 on 2024-11-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_student_admission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='admission',
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(),
        ),
    ]
