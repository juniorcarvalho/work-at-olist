from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api_book.core.models import Author, Book
from .serializers import BookSerializer, AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    '''
    view for Author
    '''
    http_method_names = ['get']
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']


class BookViewSet(viewsets.ModelViewSet):
    '''
    view for Book
    '''
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'edition', 'publication_year', 'authors']
    lookup_field = 'id'
