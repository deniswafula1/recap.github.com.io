# Generated by Django 5.1.2 on 2024-11-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission',
            field=models.CharField(max_length=30),
        ),
    ]