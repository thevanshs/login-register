# Generated by Django 4.0 on 2024-01-31 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logref', '0003_student_remove_userprofile_user_delete_people_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='fname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='lname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]