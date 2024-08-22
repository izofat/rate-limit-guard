import random

import pytest

from tests.config import TEST_ENDPOINTS, TEST_URL


@pytest.fixture
def endpoint():
    random_endpoint = random.choice(TEST_ENDPOINTS)
    return TEST_URL + random_endpoint


@pytest.fixture
def index():
    return random.randint(1, 20)


@pytest.fixture
def url(request):
    test_endpoint = request.getfixturevalue("endpoint")
    test_index = request.getfixturevalue("index")
    return f"{test_endpoint}/{test_index}"
