# Generated by Django 4.1.1 on 2023-04-30 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yogaapp', '0025_alter_salary_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yogaapp.registeredinstructor'),
        ),
    ]
