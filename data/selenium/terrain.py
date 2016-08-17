from lettuce import before, after, world
from selenium import webdriver
import reset_db
import lettuce_webdriver.webdriver

# http://lettuce.it/reference/terrain.html

@before.all
def setup_browser():

    # setup the browser
    world.browser = webdriver.Chrome()
    world.browser.set_window_size(1024, 768)
    world.browser.set_window_position(128, 0)

@before.each_feature
def reset_database_and_browser(feature):

    # clean the database
    reset_db.reset_database()

    # delete all cookies
    world.browser.delete_all_cookies()

# https://github.com/bbangert/lettuce_webdriver/blob/master/lettuce_webdriver/css_selector_steps.py

@after.all
def tear_down_feature(feature):
    world.browser.quit()
