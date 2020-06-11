# coding=utf-8

from configparser import ConfigParser

# python3中所有未指定父类的都默认继承自object类
class ConfigReader():
    _instance = None # instance 实例

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs) # super代表当前类的父类
        return cls._instance
        # return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read("config/config.ini")

    def get_db(self, option):
        return self.cf.get("db", option)

    def get_email(self, option):
        return self.cf.get("email", option)

    def get_project(self, option):
        return self.cf.get("project", option)

# print(ConfigReader().get_project('host'))

