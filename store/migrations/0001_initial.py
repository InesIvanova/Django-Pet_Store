# Generated by Django 2.1.7 on 2019-02-25 13:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=20)),
                ('age', models.PositiveIntegerField(blank=True, default='unknown')),
                ('kind', models.CharField(blank=True, choices=[('dog', 'Dog'), ('cat', 'Cat'), ('unknown', 'No information')], default='unknown', max_length=20)),
                ('breed', models.CharField(blank=True, default='unknown', max_length=20)),
                ('color', models.CharField(choices=[('0', 'blue'), ('1', 'green'), ('2', 'red'), ('3', 'cyan'), ('4', 'magenta'), ('5', 'yellow'), ('6', 'black'), ('7', 'white')], max_length=20)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('image', models.ImageField(default='C:/Users/Ines/Desktop/SoftUniStudents/Django/PetStore-Django/Scripts/PetStore/store/static/images/default.jpg', upload_to='C:/Users/Ines/Desktop/SoftUniStudents/Django/PetStore-Django/Scripts/PetStore/store/static/images')),
            ],
        ),
    ]
