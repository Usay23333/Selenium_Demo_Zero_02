# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

gc = webdriver.Chrome()

gc.get(r"D:\PythonProjects\Selenium_Demo_Zero_02\Test_Selenium.html")
gc.maximize_window()
sleep(1)

gc.find_element(By.XPATH, "//input[@value='点我测试prompt弹框']").click()
sleep(1)

gc.switch_to.alert.send_keys("hello") # 往prompt弹框中输入内容
sleep(1)
gc.switch_to.alert.accept() # 点击prompt弹框中的确定
# gc.switch_to.alert.dismiss() # 点击prompt弹框中的取消