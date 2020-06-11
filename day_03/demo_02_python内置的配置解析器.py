# coding=utf-8

from configparser import ConfigParser

cf = ConfigParser()
cf.read("config/config.ini")

bbs_host = cf.get("project", "host")
bbs_port = cf.get("project", "port")
bbs_path = cf.get("project", "path")
url = f"{bbs_host}:{bbs_port}/{bbs_path}"
print(url)


