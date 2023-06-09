# Generated by Django 4.1.1 on 2023-04-28 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yogaapp', '0021_product_gst_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yogaapp.courses')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yogaapp.registeredinstructor')),
            ],
        ),
        migrations.DeleteModel(
            name='SalaryAllotment',
        ),
    ]
