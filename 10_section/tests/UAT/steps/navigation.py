from behave import *
from selenium import webdriver


use_step_matcher('re')


@given('I am on the Homepage')
def step_impl(context):
    brouser = webdriver.Chrome("C:\drivers")
    brouser.get("http://127.0.0.1:5000")