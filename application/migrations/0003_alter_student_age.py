# Generated by Django 5.1.2 on 2024-11-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_student_admission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.CharField(max_length=30),
        ),
    ]
