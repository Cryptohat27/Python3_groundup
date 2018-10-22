"""

"""

import pytest

@pytest.yield_fixture()
def setUp():
    print("Running conftest demo2 method setUp")
    yield
    print("Running conftest demo3 method tearDown")

def test_demo2_methodA(setUp):
    print("Running conftestdemo2 MethodA")

def test_demo3_methodB(setUp):
    print("Running conftest demo2 method B")
