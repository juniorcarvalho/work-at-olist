# Generated by Django 3.0.6 on 2020-05-16 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Título')),
                ('edition', models.CharField(max_length=50, verbose_name='Edição')),
                ('publication_year', models.IntegerField(verbose_name='Ano da Publicação')),
                ('authors', models.ManyToManyField(related_name='book_authors', to='core.Author')),
            ],
        ),
    ]