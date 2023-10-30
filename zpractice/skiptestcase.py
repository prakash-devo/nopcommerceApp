import pytest


@pytest.mark.login()
def test1():
    print("this is test case 1")

@pytest.mark.skip("this is or skip")
def test2():
    print("this is test case 2")
@pytest.mark.login()
def test3():
    print("this is test case 3")


