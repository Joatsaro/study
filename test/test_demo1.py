# Any pytest file should start with test_
# pytest method names should start with test
# any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution
# -s logs in output
# -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip

import pytest

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail
def test_greetCreditCard():
    print("Good Morning")

@pytest.fixture()
def setup():
    print("I will be executing first")

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

