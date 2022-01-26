from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from nose.tools import assert_equal, assert_true

def before_all(context):
	context.browser = webdriver.Firefox()
	context.browser.maximize_window()

def after_all(context):
	context.browser.quit()