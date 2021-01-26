# Generated by Django 3.1.2 on 2020-12-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20201201_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('education', 'Education'), ('entertainment', 'Entertainment'), ('thesis', 'Thesis'), ('biography', 'Biography'), ('history', 'History'), ('essay', 'Essay'), ('paper/article', 'Paper/Article')], default='education', max_length=30),
        ),
    ]