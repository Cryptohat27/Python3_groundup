import pytest

@pytest.yield_fixture()
def setUp():
    print("Running conftest demo1 method setUp")
    yield
    print("Running conftest demo1 method tearDown")

def test_demo1_methodA(setUp):
    print("running conftest demo1 method A")

def test_demo1_methodB(setUp):
    print("running conftest demo1 method B")
