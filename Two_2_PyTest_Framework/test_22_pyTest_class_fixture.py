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
# @pytest.fixture() this is similar to Before and After Tests,Methods,Suites in testNG
# yield is used to run methods after the Main Test Case.
# Created conftest.py file, Testcases which are used by everyfile are placed here, so that repeatation of code are avoided.

# @pytest.fixture(scope='class') Instead of mentioning fixture as an argument to every method,
#                                       we can directly mentioned it to class and it will be applicable to all the methods in the class
# @pytest.mark.usefixtures("dataDriver") This is used to inject the data during test execution for the test cases to validate

# @pytest.fixture(params=["Chrome","Firefox","Edge",("sid","007"),("harsh","007")])
# We can also use this way to pass the values using the params options
@pytest.mark.usefixtures("test_addition")
class TestExamples:
    def test_addingStuff1(self):
        print("stuffs are added1, later ")

    def test_addingStuff2(self):
        print("stuffs are added2, later ")

    def test_addingStuff3(self):
        print("stuffs are added3, later ")



