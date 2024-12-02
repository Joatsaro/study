# Any pytest file should start with test_
# pytest method names should start with test
# any code should be wrapped in method only
import pytest

@pytest.mark.smoke
# @pytest.mark.skip
def test_firstProgram():
    msg = "Hello" # operations
    assert msg == "Hi", "test failed because strings do not match"

def test_SecondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"
