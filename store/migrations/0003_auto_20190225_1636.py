# Generated by Django 2.1.7 on 2019-02-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190225_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(default='C:/Users/Ines/Desktop/SoftUniStudents/Django/PetStore-Django/Scripts/PetStore/store/static/images/default.jpg', max_length=500, upload_to='C:/Users/Ines/Desktop/SoftUniStudents/Django/PetStore-Django/Scripts/PetStore/store/static/images'),
        ),
    ]