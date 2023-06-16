# -*- coding:cp949 -*-
# 모든 최상위 수준의 윈도우를 나열합니다.
import win32gui
 
def EnumWindowsHandler(hwnd, extra):
	wintext = win32gui.GetWindowText(hwnd)
	print "%08X: %s" % (hwnd, wintext)
 
if __name__ == '__main__':
	win32gui.EnumWindows(EnumWindowsHandler, None)