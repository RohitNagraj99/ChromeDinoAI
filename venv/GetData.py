from selenium import webdriver
import selenium.webdriver.common.keys as Keys
import time
import threading
import CaptureVideo

driver = webdriver.Chrome('/home/rohit/Work/chromedriver')

driver.get('chrome://dino')
time.sleep(1)

page = driver.find_element_by_class_name('offline')

#page.send_keys(u'\ue00d')

CaptureVideo.start()