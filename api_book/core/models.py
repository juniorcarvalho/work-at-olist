from django.db import models


class Author(models.Model):
    '''
    Model for Author
    '''
    name = models.CharField('Autor', max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    '''
    Model for Book
    '''

    name = models.CharField('Título', max_length=100)
    edition = models.CharField('Edição', max_length=50)
    publication_year = models.IntegerField('Ano da Publicação')
    authors = models.ManyToManyField(Author, related_name='book_authors')

    def __str__(self):
        return self.name
