from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from nose.tools import assert_equal, assert_true

@when('the user visits the "{page}" page')
def step(context, page):
   if page == "home":
      context.browser.get('http://localhost:8080/')
   elif page == "accelerator-dashboard":
      context.browser.get('http://localhost:8080/accelerator-dashboard')
   elif page == "job-search":
      context.browser.get('http://localhost:8080/search')
   elif page == "cart":
      context.browser.get('http://localhost:8080/cart')

@when('the user can click on the "{tab}" tab')
def step(context, tab):
   wait = WebDriverWait(context.browser, 10)
   if tab == "Home":
      element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div > div > ul > a > li")))
      element.click()
   elif tab == "Find Jobs":
      element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div > div > ul > a:nth-child(3) > li")))
      element.click()
   elif tab == "Job Cart":
      element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div > div > ul > a.router-link-exact-active.router-link-active > li")))
      element.click()

@then('the user ends up on the {page} page')
def step(context, page):
   wait = WebDriverWait(context.browser, 10)
   if page == "Home":
      element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dashboard > div > div:nth-child(1) > div > div.card-body > h4 > strong"))).text
      assert_equal(element.text, "Recommend Jobs to an Employee")
   elif page == "Find Jobs":
      element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search > div > div > h4"))).text
      assert_equal(element.text, "Recommended For You")
   elif page == "cart":
      element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart > div.mb-4.card > div > h4"))).text
      assert_equal(element.text, "Job Cart")

@then('the user sees the name "{name}"')
def step(context, name):
   wait = WebDriverWait(context.browser, 10)
   actualName = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dashboard > div > div:nth-child(2) > div > div.card-body > h4 > strong"))).text
   assert_equal(name, actualName)

@then('the user sees the title "{title}"')
def step(context, title):
   wait = WebDriverWait(context.browser, 10)
   titleLine = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#dashboard > div > div:nth-child(2) > div > div.card-body > p:nth-child(3)'))).text
   assert(titleLine.find(title))

@then('the user sees the Employee Id "{employeeId}"')
def step(context, employeeId):
   wait = WebDriverWait(context.browser, 10)
   employeeIdLine = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#dashboard > div > div:nth-child(2) > div > div.card-body > p:nth-child(4)'))).text
   assert(employeeIdLine.find(employeeId))

@then('the user sees the Clearence Level "{clearenceLevel}"')
def step(context, clearenceLevel):
   wait = WebDriverWait(context.browser, 10)
   clearenceLevelLine = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#dashboard > div > div:nth-child(2) > div > div.card-body > p:nth-child(5)'))).text
   assert(clearenceLevelLine.find(clearenceLevel))

@When('the user clicks the Find Jobs button')
def step(context):
   wait = WebDriverWait(context.browser, 10)
   clearenceLevelLine = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#dashboard > div > div:nth-child(1) > div > div.links-light.profile-card-footer.card-footer > a > button'))).click

@When('the user finds the employee "{eid}"')
def step(context, eid):
   wait = WebDriverWait(context.browser, 10)
   inputBox = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#user')))
   inputBox.send_keys(eid)
   button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dashboard > div > div:nth-child(1) > div > div.card-body > div > form > div.links-light.profile-card-footer.card-footer > button")))
   button.click()

@Then('the user finds employee name "{name}"')
def step(context, name):
   context.browser.implicitly_wait(20)
   wait = WebDriverWait(context.browser, 10)
   nameLine = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dashboard > div > div:nth-child(2) > div > div.card-body > h4 > strong"))).text
   assert(nameLine.find(name))

@Then('employee workday profile does not exist')
def step(context):
   try:
      context.browser.find_element_by_css_selector("#dashboard > div > div:nth-child(2) > div")
   except NoSuchElementException:
      return False
   return True
