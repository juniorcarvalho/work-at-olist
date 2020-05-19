import pytest

from api_book.core.models import Author


@pytest.mark.django_db
def test_view_author_get_return_status_code_200(client_api, api_author_1, api_author_2):
    '''
    test status_code = 200 and json result for Author ViewSet
    '''
    response = client_api.get('/api/authors/', format='json')

    assert response.status_code == 200
    assert response.json() == {
        'count': 2,
        'next': None,
        'previous': None,
        'results': [
            {
                'id': api_author_1.id,
                'name': api_author_1.name,
            },
            {
                'id': api_author_2.id,
                'name': api_author_2.name
            }
        ]
    }


@pytest.mark.django_db
def test_view_author_get_return_status_code_200_with_filter_name(client_api, api_author_1, api_author_2):
    '''
    test status_code = 200 and json result for Author ViewSet with filter name
    '''
    response = client_api.get(f'/api/authors/?name={api_author_2.name}', format='json')

    assert response.status_code == 200
    assert response.json() == {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [
            {
                'id': api_author_2.id,
                'name': api_author_2.name
            }
        ]
    }


@pytest.mark.django_db
def test_view_author_get_return_status_code_200_and_pagination(client_api):
    '''
    test status_code = 200 and pagination for Author ViewSet
    '''
    for count in range(0, 30):
        Author.objects.create(
            name=f'Author: {count}'
        )

    response = client_api.get('/api/authors/', format='json')

    assert response.status_code == 200
    assert response.json()['count'] == 30
    assert response.json()['next']

    next_url = response.json()['next']

    response = client_api.get(next_url, format='json')

    assert response.status_code == 200
    assert response.json()['count'] == 30
    assert response.json()['previous']
