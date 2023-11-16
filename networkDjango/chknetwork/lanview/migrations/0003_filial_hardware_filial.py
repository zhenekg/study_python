# Generated by Django 4.2.3 on 2023-08-16 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lanview', '0002_category_hardware_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='hardware',
            name='filial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lanview.filial'),
        ),
    ]