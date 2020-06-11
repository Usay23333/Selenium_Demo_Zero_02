# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from pykeyboard import PyKeyboard
import pyperclip as pyc
import os

driver = webdriver.Chrome() # 实例化一个浏览器对象
driver.get("https://ssxxlive.top/images/1.jpg")
driver.maximize_window()
sleep(2)

pic = driver.find_element(By.CSS_SELECTOR, "img")
ActionChains(driver).context_click(pic).perform()

kb = PyKeyboard()
kb.tap_key('v')
sleep(3)

kb.press_keys([kb.control_key, 'x'])
pic_name = pyc.paste()
print(pic_name)

pic_dir = "pics"
if not os.path.exists(pic_dir):
    os.mkdir(pic_dir)

full_path = os.path.join(os.path.abspath(pic_dir), pic_name) # pics/1.jpg
pyc.copy(full_path)

kb.press_keys([kb.control_key, 'v'])

kb.tap_key(kb.tab_key)
kb.tap_key(kb.tab_key)

kb.tap_key(kb.enter_key)

