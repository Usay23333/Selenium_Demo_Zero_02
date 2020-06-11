# coding=utf-8

from selenium import webdriver
from configreader import ConfigReader

# gc = webdriver.Chrome()

cr = ConfigReader()
cr1 = ConfigReader()
cr2 = ConfigReader()

host = ConfigReader().get_project("host")
port = ConfigReader().get_project("port")
path = ConfigReader().get_project("path")
print(f"{host}:{port}/{path}")

print(id(cr.cf))
print(id(cr1.cf))
print(id(cr2.cf))
# gc.get(f"{host}:{port}/{path}")