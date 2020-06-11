# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from pykeyboard import PyKeyboard
import pyperclip as pyc

driver = webdriver.Chrome() # 实例化一个浏览器对象
driver.get(r"D:\PythonProjects\Selenium_Demo_Zero_02\Test_Selenium.html")
driver.maximize_window()
sleep(2)

ActionChains(driver).click(driver.find_element(By.XPATH, "//input[@type='file']")).perform()

sleep(2)
kb = PyKeyboard()

# tap_key 单击
kb.tap_key(kb.shift_key) # 按下shift

path = r"C:\Users\zero\Desktop\test滴滴test.jpg"

# kb.type_string(path) # 打字：指定文本

pyc.copy(path)
kb.press_keys([kb.control_key, 'v'])

# p = pyc.paste()
# print(p)

sleep(0.5)
kb.tap_key(kb.tab_key)
kb.tap_key(kb.tab_key)
kb.tap_key(kb.enter_key)