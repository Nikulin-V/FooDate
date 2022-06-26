# Generated by Django 4.0.5 on 2022-06-26 18:25

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0003_alter_productcard_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productcard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='book.productcard')),
                ('amount', models.FloatField(null=True, verbose_name='Количество продукта')),
                ('amount_unit', models.CharField(choices=[('мг', 'миллиграммы'), ('г', 'граммы'), ('кг', 'килограммы'), ('мл', 'миллилитры'), ('л', 'литры')], max_length=2, null=True, verbose_name='Единица измерения количества продукта')),
                ('production_date', models.DateTimeField(null=True, validators=[django.core.validators.MaxValueValidator(datetime.datetime(2022, 6, 26, 23, 25, 15, 497215))], verbose_name='Дата изготовления')),
                ('purchase_date', models.DateTimeField(null=True, validators=[django.core.validators.MaxValueValidator(datetime.datetime(2022, 6, 26, 23, 25, 15, 497215))], verbose_name='Дата покупки')),
            ],
            options={
                'abstract': False,
            },
            bases=('book.productcard',),
            managers=[
                ('products', django.db.models.manager.Manager()),
            ],
        ),
    ]
