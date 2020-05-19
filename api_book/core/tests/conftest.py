import pytest

from api_book.core.models import Author, Book


@pytest.fixture
@pytest.mark.django_db
def author_1():
    return Author.objects.create(name='Author 1 test')


@pytest.fixture
@pytest.mark.django_db
def author_2():
    return Author.objects.create(name='Author 2 test')


@pytest.fixture
@pytest.mark.django_db
def book(author_1, author_2):
    book = Book(
        name='book test 1',
        edition='First edition',
        publication_year=2020,
    )
    book.save()
    book.authors.add(author_1)
    book.authors.add(author_2)
    return book
