# Generated by Django 4.0.3 on 2022-12-29 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('private', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='private.college')),
            ],
        ),
    ]
