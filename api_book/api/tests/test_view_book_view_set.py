import pytest

from api_book.core.models import Book


@pytest.mark.django_db
def test_view_book_get_return_status_code_200(client_api, api_book_1, api_book_2):
    '''
    test status_code = 200 and json result for Book ViewSet
    '''
    response = client_api.get('/api/books/', format='json')

    assert response.status_code == 200
    assert response.json() == {
        'count': 2,
        'next': None,
        'previous': None,
        'results': [
            {
                'id': api_book_1.id,
                'name': api_book_1.name,
                'edition': api_book_1.edition,
                'publication_year': api_book_1.publication_year,
                'authors': [
                    {
                        'id': api_book_1.authors.all()[0].id,
                        'name': api_book_1.authors.all()[0].name,
                    },
                    {
                        'id': api_book_1.authors.all()[1].id,
                        'name': api_book_1.authors.all()[1].name,
                    }
                ]
            },
            {
                'id': api_book_2.id,
                'name': api_book_2.name,
                'edition': api_book_2.edition,
                'publication_year': api_book_2.publication_year,
                'authors': [
                    {
                        'id': api_book_2.authors.all()[0].id,
                        'name': api_book_2.authors.all()[0].name,
                    },
                ]
            }
        ]
    }


@pytest.mark.django_db
def test_view_book_get_return_status_code_200_with_filter_name(client_api, api_book_1, api_book_2):
    '''
    test status_code = 200 and json result for Book ViewSet with filter name
    '''
    response = client_api.get(f'/api/books/?name={api_book_2.name}', format='json')

    assert response.status_code == 200
    assert response.json() == {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [
            {
                'id': api_book_2.id,
                'name': api_book_2.name,
                'edition': api_book_2.edition,
                'publication_year': api_book_2.publication_year,
                'authors': [
                    {
                        'id': api_book_2.authors.all()[0].id,
                        'name': api_book_2.authors.all()[0].name,
                    },
                ]
            }
        ]
    }


@pytest.mark.django_db
def test_view_book_get_return_status_code_200_with_filter_edition(client_api, api_book_1, api_book_2):
    '''
    test status_code = 200 and json result for Book ViewSet with filter edition
    '''
    response = client_api.get(f'/api/books/?edition={api_book_2.edition}', format='json')

    assert response.status_code == 200
    assert response.json() == {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [
            {
                'id': api_book_2.id,
                'name': api_book_2.name,
                'edition': api_book_2.edition,
                'publication_year': api_book_2.publication_year,
                'authors': [
                    {
                        'id': api_book_2.authors.all()[0].id,
                        'name': api_book_2.authors.all()[0].name,
                    },
                ]
            }
        ]
    }


@pytest.mark.django_db
def test_view_book_get_return_status_code_200_with_filter_publication_year(client_api, api_book_1, api_book_2):
    '''
    test status_code = 200 and json result for Book ViewSet with filter publication_year
    '''
    response = client_api.get(f'/api/books/?publication_year={api_book_2.publication_year}', format='json')

    assert response.status_code == 200
    assert response.json() == {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [
            {
                'id': api_book_2.id,
                'name': api_book_2.name,
                'edition': api_book_2.edition,
                'publication_year': api_book_2.publication_year,
                'authors': [
                    {
                        'id': api_book_2.authors.all()[0].id,
                        'name': api_book_2.authors.all()[0].name,
                    },
                ]
            }
        ]
    }


@pytest.mark.django_db
def test_view_book_get_return_status_code_200_with_filter_authors(client_api, api_book_1, api_book_2):
    '''
    test status_code = 200 and json result for Book ViewSet with filter authors
    '''
    response = client_api.get(f'/api/books/?authors={api_book_2.authors.all()[0].id}', format='json')

    assert response.status_code == 200
    assert response.json() == {
        'count': 2,
        'next': None,
        'previous': None,
        'results': [
            {
                'id': api_book_1.id,
                'name': api_book_1.name,
                'edition': api_book_1.edition,
                'publication_year': api_book_1.publication_year,
                'authors': [
                    {
                        'id': api_book_1.authors.all()[0].id,
                        'name': api_book_1.authors.all()[0].name,
                    },
                    {
                        'id': api_book_1.authors.all()[1].id,
                        'name': api_book_1.authors.all()[1].name,
                    },
                ]
            },
            {
                'id': api_book_2.id,
                'name': api_book_2.name,
                'edition': api_book_2.edition,
                'publication_year': api_book_2.publication_year,
                'authors': [
                    {
                        'id': api_book_2.authors.all()[0].id,
                        'name': api_book_2.authors.all()[0].name,
                    },
                ]
            }
        ]
    }


@pytest.mark.django_db
def test_view_book_get_return_status_code_200_and_pagination(client_api, api_author_1, api_author_2):
    '''
    test status_code = 200 and pagination for Book ViewSet
    '''
    for count in range(0, 30):
        book = Book(
            name=f'Book: {count}',
            edition=f'Edition: {count}',
            publication_year=2020 - count,
        )
        book.save()
        if count % 2 == 0:
            book.authors.add(api_author_1)
            book.authors.add(api_author_2)
        else:
            book.authors.add(api_author_2)

    response = client_api.get('/api/books/', format='json')

    assert response.status_code == 200
    assert response.json()['count'] == 30
    assert response.json()['next']

    next_url = response.json()['next']

    response = client_api.get(next_url, format='json')

    assert response.status_code == 200
    assert response.json()['count'] == 30
    assert response.json()['previous']


@pytest.mark.django_db
def test_view_book_get_by_id_return_status_code_200(client_api, api_book_1, api_book_2):
    '''
    test status_code = 200 and json result for Book ViewSet with id
    '''
    response = client_api.get(f'/api/books/{api_book_2.id}/', format='json')

    assert response.status_code == 200
    assert response.json() == {
        'id': api_book_2.id,
        'name': api_book_2.name,
        'edition': api_book_2.edition,
        'publication_year': api_book_2.publication_year,
        'authors': [
            {
                'id': api_book_2.authors.all()[0].id,
                'name': api_book_2.authors.all()[0].name
            }
        ]
    }


@pytest.mark.django_db
def test_view_book_get_by_id_return_status_code_404(client_api):
    '''
    test status_code = 404 and json result for Book ViewSet with id not found
    '''
    response = client_api.get('/api/books/999/', format='json')

    assert response.status_code == 404
    assert response.json() == {
        'detail': 'Não encontrado.'
    }


@pytest.mark.django_db
def test_view_book_post_return_status_code_201(client_api, api_author_1, api_author_2):
    '''
    test status_code == 201 and json result for post Book model
    '''
    payload = {
        'name': 'book test 1',
        'edition': 'first edition',
        'publication_year': 2020,
        'authors_id': [api_author_1.id, api_author_2.id]
    }

    response = client_api.post('/api/books/', format='json', data=payload)

    assert response.status_code == 201
    assert response.json() == {
        'id': response.json()['id'],
        'name': payload['name'],
        'edition': payload['edition'],
        'publication_year': payload['publication_year'],
        'authors': [
            {
                'id': api_author_1.id,
                'name': api_author_1.name,
            },
            {
                'id': api_author_2.id,
                'name': api_author_2.name,
            },
        ]
    }


@pytest.mark.django_db
def test_view_book_put_return_status_code_200(client_api, api_book_1, api_author_2):
    '''
    test status_code == 200 and json result for put Book model
    '''
    payload = {
        'name': 'book test 2',
        'edition': 'second edition',
        'publication_year': 2019,
        'authors_id': [api_author_2.id]
    }

    response = client_api.put(f'/api/books/{api_book_1.id}/', format='json', data=payload)

    assert response.status_code == 200
    assert response.json() == {
        'id': api_book_1.id,
        'name': payload['name'],
        'edition': payload['edition'],
        'publication_year': payload['publication_year'],
        'authors': [
            {
                'id': api_author_2.id,
                'name': api_author_2.name,
            }
        ]

    }


@pytest.mark.django_db
def test_view_book_put_return_status_code_404(client_api):
    '''
    test status_code == 404 for put Book model
    '''
    response = client_api.put('/api/books/999/', format='json', data={})

    assert response.status_code == 404
    assert response.json() == {
        'detail': 'Não encontrado.'
    }


@pytest.mark.django_db
def test_view_book_delete_return_status_code_204(client_api, api_book_1):
    '''
    test status_code == 204 for delete Book model
    '''
    response = client_api.delete(f'/api/books/{api_book_1.id}/', format='json')

    assert response.status_code == 204


@pytest.mark.django_db
def test_view_book_delete_return_status_code_404(client_api):
    '''
    test status_code == 404 for delete Book model
    '''
    response = client_api.delete('/api/books/999/', format='json', data={})

    assert response.status_code == 404
    assert response.json() == {
        'detail': 'Não encontrado.'
    }
