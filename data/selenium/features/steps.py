from lettuce import *
from lettuce_webdriver.util import (assert_false,
                                    AssertContextManager,
                                    option_in_select)
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


# https://github.com/bbangert/lettuce_webdriver/blob/master/lettuce_webdriver/webdriver.py
# https://github.com/bbangert/lettuce_webdriver/blob/master/lettuce_webdriver/css_selector_steps.py
# https://github.com/bbangert/lettuce_webdriver/blob/master/lettuce_webdriver/util.py

@step('I set the text input, with id "(.*?)" to "(.*?)"')
def fill_in_textfield_by_id(step, field_name, value):
    with AssertContextManager(step):
        text_field = find_input_by_id(world.browser, field_name)
        text_field.clear()
        text_field.send_keys(value)

def find_input_by_id(browser, attribute):
    xpath = "//input[@id='%s']" % attribute
    elems = browser.find_elements_by_xpath(xpath)
    return elems[0] if elems else False



@step('I set the text input, with class "(.*?)" to "(.*?)"')
def fill_in_textfield_by_class(step, field_name, value):
    with AssertContextManager(step):
        text_field = find_field_by_class(world.browser, field_name)
        text_field.clear()
        text_field.send_keys(value)

def find_field_by_class(browser, attribute):
    xpath = "//input[@class='%s']" % attribute
    elems = browser.find_elements_by_xpath(xpath)
    return elems[0] if elems else False



@step('I click the "(.*?)" button')
def click_button_by_value(step, button_value):
    with AssertContextManager(step):
        button = find_button_by_value(world.browser, button_value)
        button.click()

def find_button_by_value(browser, attribute):
    xpath = "//input[@type='button' and @value='%s']" % attribute
    elems = browser.find_elements_by_xpath(xpath)
    return elems[0] if elems else False



@step('I select "(.*?)" from the dynamic select "(.*?)"')
def select_option_by_value(step, option_val, select_id):
    with AssertContextManager(step):

        # wait for jQuery to finish any Ajax calls
        driver = world.browser
        wait = WebDriverWait(driver, 30)
        wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))

        option = option_in_select(world.browser, select_id, option_val)
        option.click()



@step('I click "(.*?)" from the auto-suggest')
def click_autosuggest(step, text_val):
    with AssertContextManager(step):

        # wait for jQuery to finish any Ajax calls
        driver = world.browser
        driver.implicitly_wait(5)  # hackish, but that's jQuery :/

        wait = WebDriverWait(driver, 30)
        wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))

        elem = world.browser.find_element_by_link_text(text_val)
        elem.click()

@step('I wait up to "(.*?)" seconds for jQuery')
def jquery_wait(step, int_val):
    with AssertContextManager(step):

        # wait for jQuery to finish any Ajax calls
        driver = world.browser
        int_val = int(int_val)
        # driver.implicitly_wait(int_val)  # hackish, but that's jQuery :/
        wait = WebDriverWait(driver, int_val)
        wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))

@step('I wait "(.*?)" seconds')
def jquery_wait(step, int_val):
    with AssertContextManager(step):

        # wait for jQuery to finish any Ajax calls
        driver = world.browser
        int_val = int(int_val)
        sleep(int_val)






@step('The element with id of "(.*?)" should have the css class "(.*?)"')
def verify_css_class(step, css_id, css_class):
    with AssertContextManager(step):
        cssSelector = css_id + "." + css_class
        element = find_element_by_id(world.browser, cssSelector)

def find_element_by_id(browser, attribute):
    elems = browser.find_elements_by_css_selector(attribute)
    return elems[0] if elems else False
