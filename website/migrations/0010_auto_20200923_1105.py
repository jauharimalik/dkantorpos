# Generated by Django 3.1 on 2020-09-23 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200923_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=64, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='keranjang',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.keranjang'),
        ),
    ]
