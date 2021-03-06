# Generated by Django 3.1.2 on 2020-12-03 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_auto_20201202_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='14 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=14, unique=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
