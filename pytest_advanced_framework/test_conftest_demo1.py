"""

"""

import pytest

@pytest.yield_fixture()
def setUp():
    print("Running conftest demo1 method setUp")
    yield
    print("Running conftest demo1 method tearDown")

def test_methodA(setUp):
    print("Running method A")

def test_methodB(setUp):
    print("Running method B")
