from behave import *
from selenium import webdriver
from tests.UAT.pages.base_page import BasePage
from tests.UAT.pages.blog_page import BlogPage
from tests.UAT.pages.new_post_page import NewPostPage



use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = BasePage(context.browser)
    context.browser.get(page.url)


@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = BlogPage(context.browser)
    context.browser.get(page.url)


@given('I am on the new post page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = NewPostPage(context.browser)
    context.browser.get(page.url)


@then('I am on the homepage')
def step_impl(context):
    page = BasePage(context.browser)
    assert context.browser.current_url == page.url


@then('I am on the blog page')
def step_impl(context):
    page = BlogPage(context.browser)
    assert context.browser.current_url == page.url