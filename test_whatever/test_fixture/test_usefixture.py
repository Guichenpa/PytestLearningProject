import pytest


@pytest.mark.usefixtures("usfixture")
def test_usefixture():
    print("\nusefixtures")
