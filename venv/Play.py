from selenium import webdriver
import selenium.webdriver.common.keys as Keys
import time
import threading
import AI

driver = webdriver.Chrome('/home/rohit/Work/chromedriver')

# internet connection must be off
driver.get('chrome://dino')
time.sleep(3)

# main page to send key commands to
page = driver.find_element_by_class_name('offline')

# start game
page.send_keys(u'\ue00d')

# controls the dinosaur
while True:
    AI.predict(page)