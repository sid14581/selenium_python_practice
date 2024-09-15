import pytest


@pytest.fixture(scope='class')
def test_addition():
    a = 5
    b = 5
    assert 10 == a + b, "Numbers aren't Same"
    print(a + b, "is printing first")
    yield
    print("\nI will execute after the addingStuff method")


@pytest.fixture(scope='class')
def dataDriver():
    print("\n importing data")
    yo = ["sid", "007", "sid007@gmail.com"]
    return yo


@pytest.fixture(params=["Chrome", "Firefox", "Edge", ("sid", "007"), ("harsh", "007")])
def crossBrowser(request):
    return request.param
