# coding=utf-8

from pykeyboard import PyKeyboard
from pymouse import PyMouse
from time import sleep
m = PyMouse()
s = m.screen_size()
print(s) # (1093, 614) 1366 * 768
m.move(s[0] // 2, s[1] // 2)
sleep(1)
kb = PyKeyboard()
kb.type_string('hello')




