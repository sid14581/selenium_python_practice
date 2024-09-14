# pytest files and methods should start with test_ and class with Test
# Any code should wrap in methods
import pytest


# py.test to the test files
# py.test -v  for verbose
# py.test -v -s  print with Output
# In py.test methods should not be with same name otherwise they get override
# give the files name to run the specific test case  py.test <file-name> -v -s
# py.test -k <specific testcase name> -v -s it will run only specific test cases
# py.test -m <smoke> -v -s [@pytest.mark.smoke] We can mark MARK test-cases which we can run collectivily like smoke & regression testing.
# [@pytest.mark.smoke] To Skip the test cases
# @pytest.mark.xfail This will run the test cases irrespective of right or wrong

@pytest.mark.skip
@pytest.mark.smoke
def test_secondProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings are not matching"


def test_addition():
    a = 5
    b = 5
    assert 10 == a + b, "Numbers aren't Same"


@pytest.mark.xfail
def test_addingStuff():
    print("stuffs are added")
