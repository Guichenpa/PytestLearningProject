import pytest


@pytest.mark.run(order=1)
def test_login():
    print("Login.....")


@pytest.mark.run(order=4)
def test_search():
    print("Search.....")


@pytest.mark.run(order=3)
def test_order():
    print("Order.....")


@pytest.mark.run(order=2)
def test_pay():
    print("Pay.....")
