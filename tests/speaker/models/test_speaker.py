from urllib.parse import urlparse, parse_qs

import pytest
from model_mommy import mommy


@pytest.fixture
def speaker():
    return mommy.prepare('speaker.Speaker',
                         first_name='Tracy',
                         last_name='Doe',
                         image_url=None,
                         email='tracy.doe@random.mail.com')


def test_name(speaker):
    assert speaker.name == 'Tracy Doe'

def test_photo(speaker):
    url = urlparse(speaker.photo)
    assert url.path == '/avatar/2b71f83c7eb72f46ce832f225861e332.jpg'
    assert  parse_qs(url.query) == {'r': ['g'],
                                    's': ['80'],
                                    'd': ['retro']}

def test_photo_with_image_url(speaker):
    speaker.image_url = 'http://site.com/image.jpg'
    assert speaker.photo == 'http://site.com/image.jpg'


def test_facebook_url(speaker):
    speaker.facebook = 'mary.doe'
    assert "https://facebook.com/mary.doe"


def test_twitter_url(speaker):
    speaker.twitter = 'mary.doe'
    assert "https://twitter.com/mary.doe"


def test_linkedin_url(speaker):
    speaker.linkedin = 'mary.doe'
    assert "https://www.linkedin.com/in/mary.doe"


def test_github_url(speaker):
    speaker.github = 'mary.doe'
    assert "https://github.com/mary.doe"


def test_behance_url(speaker):
    speaker.behance = 'mary.doe'
    assert "https://www.behance.net/mary.doe"


def test_medium_url(speaker):
    speaker.medium = 'mary.doe'
    assert "https://medium.com/mary.doe"
