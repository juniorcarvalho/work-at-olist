from django.conf import settings

from api_book.core.apps import CoreConfig


def test_app_core_name():
    '''
    test if app core name is configured
    '''
    assert CoreConfig.name == 'core'


def test_app_core_is_configured():
    '''
    test if app is configured in settings
    '''
    assert 'api_book.core' in settings.INSTALLED_APPS
