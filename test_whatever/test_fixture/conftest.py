import pytest


# @pytest.fixture(scope="session")
# def test_session():
#     print("                                            我是Session级别的fixture")
#
#
# @pytest.fixture(scope="function")
# def test_func1():
#     print("----------------------我是function级别的fixture----------------------")


@pytest.fixture(scope="function")
def get_param():
    params = {
        'tel': '13947948806'
    }
    return params


@pytest.fixture(scope="function", autouse=True)
def 前置后置步骤():
    print("----------------------我是前置步骤----------------------")
    yield
    print("----------------------我是后置步骤----------------------")
    print("\n")


@pytest.fixture(scope="function")
def use_fixture(get_param):
    print("我现在使用usefixture")
