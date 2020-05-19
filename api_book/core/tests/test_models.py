import pytest


@pytest.mark.django_db
def test_model_author(author_1):
    '''
    test model author
    '''
    assert str(author_1) == author_1.name


@pytest.mark.django_db
def test_model_book(book):
    '''
    test model book
    '''
    assert str(book) == book.name
    assert book.authors.count() == 2
