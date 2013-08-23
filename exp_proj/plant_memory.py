# -*- coding: utf-8 -*-

import mymodel as my
import win32gui as gui
import win32process as p



hwnd = gui.FindWindowEx(None, None, "MainWindow", "ֲ植物大战僵尸中文版")

pid = my.getWindowPid(hwnd)

print ("当前阳光数:", my.readGameIntType(pid, '6a9ec0', '768', '5560'))

base = my.anyto10('6a9ec0')
base1 = my.anyto10('768')
base2 = my.anyto10('5560')


offset1 = my.readMemoryIntType(pid, base) + base1
address = my.readMemoryIntType(pid, offset1) + base2

value = input('Please Enter Your Value > ')
my.writeMemoryIntType(pid, address, int(value))