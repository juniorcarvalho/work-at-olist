import pytest
from rest_framework.test import APIClient

from api_book.core.models import Author, Book

client = APIClient()


@pytest.fixture
def client_api():
    return client


@pytest.fixture
@pytest.mark.django_db
def api_author_1():
    return Author.objects.create(name='Author 1 test')


@pytest.fixture
@pytest.mark.django_db
def api_author_2():
    return Author.objects.create(name='Author 2 test')


@pytest.fixture
@pytest.mark.django_db
def api_book_1(api_author_1, api_author_2):
    book = Book(
        name='book test 1',
        edition='First edition',
        publication_year=2020,
    )
    book.save()
    book.authors.add(api_author_1)
    book.authors.add(api_author_2)
    return book


@pytest.fixture
@pytest.mark.django_db
def api_book_2(api_author_2):
    book = Book(
        name='book test 2',
        edition='Second edition',
        publication_year=2019,
    )
    book.save()
    book.authors.add(api_author_2)
    return book
