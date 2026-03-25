import pytest
import allure

@allure.title("TC#0 - verify that 0-0 is equal to 0")
@allure.description("This is a smoke Testcase which check - verify that 0-0 is equal to 0")
@pytest.mark.smoke
def test_sub0():
    assert 0-0 ==0

@allure.title("TC#1 - verify that 1-1 is equal to 0")
@allure.description("This is a smoke Testcase which check - verify that 1-1 is equal to 0")
@pytest.mark.smoke
def test_sub1():
    assert 1-1 ==0

@allure.title("TC#2 - verify that 2-2 is equal to 0")
@allure.description("This is a regression Testcase which check - verify that 2-2 is equal to 0")
@pytest.mark.regression
def test_sub2():
    assert 2-2 ==0

@allure.title("TC#3 - verify that 3-3 is equal to 0")
@allure.description("This is a sanity Testcase which check - verify that 3-3 is equal to 0")
@pytest.mark.sanity
def test_sub3():
    assert 3-3 ==0

@pytest.mark.skip(reason="Not Working, Skip it.")
def test_sub4():
    assert 4-4 !=0