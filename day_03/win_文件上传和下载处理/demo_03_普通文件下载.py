# coding=utf-8

from selenium import webdriver
from time import sleep
import os

options = webdriver.ChromeOptions()
files_path = os.path.join(os.path.abspath(os.path.pardir),'download_files')
if not os.path.exists(files_path):
    os.mkdir(files_path)
print(files_path)

prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': files_path, "download.prompt_for_download": False, "safebrowsing.enabled": True}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=options)
driver.get("https://www.jjxsw.la/txt/dl-47-34909.html")
driver.maximize_window()

sleep(3)
driver.find_element_by_xpath("//*[@id='Frame']/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/a[3]").click()
