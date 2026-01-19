import pytest

# these fixtures will help pytest understand when and how to run
# preWork is passed into the two functions and it is defined with scope as function
# so it will run before each function in this file
@pytest.fixture(scope="function")
# we can use module as well in the scope to run only once before all tests in the module or the test file
def preWork():
    print("I setup browser instance")

# pytest adding test in the prefix will consider it as a test
# Just like @test annotation in testNG
def test_initialChecks(preWork):
    print("This is first test")

def test_secondChecks(preWork):
    print("This is second test")

