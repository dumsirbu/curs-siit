# Generated by Django 4.0.5 on 2022-06-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curs', '0004_alter_student_nume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
