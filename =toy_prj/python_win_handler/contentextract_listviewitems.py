# -*- coding:cp949 -*-
import win32gui
import win32api
import commctrl
import struct
import ctypes
 
from win32con import PAGE_READWRITE, MEM_COMMIT, MEM_RESERVE, MEM_RELEASE, PROCESS_ALL_ACCESS
 
GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId
VirtualAllocEx           = ctypes.windll.kernel32.VirtualAllocEx
VirtualFreeEx            = ctypes.windll.kernel32.VirtualFreeEx
OpenProcess              = ctypes.windll.kernel32.OpenProcess
WriteProcessMemory       = ctypes.windll.kernel32.WriteProcessMemory
ReadProcessMemory        = ctypes.windll.kernel32.ReadProcessMemory
 
def GetListViewItems(hwnd, column_index=0):
	# Allocate virtual memory inside target process
	pid   = ctypes.create_string_buffer(4)
	p_pid = ctypes.addressof(pid)
 
	GetWindowThreadProcessId(hwnd, p_pid) # process owning the given hwnd
	hProcHnd = OpenProcess(PROCESS_ALL_ACCESS, False, struct.unpack("i",pid)[0])
	pLVI    = VirtualAllocEx(hProcHnd, 0, 4096, MEM_RESERVE|MEM_COMMIT, PAGE_READWRITE)
	pBuffer = VirtualAllocEx(hProcHnd, 0, 4096, MEM_RESERVE|MEM_COMMIT, PAGE_READWRITE)
 
	# Prepare an LVITEM record and write it to target process memory
	lvitem_str    = struct.pack('iiiiiiiii', *[0,0,column_index,0,0,pBuffer,4096,0,0])
	lvitem_buffer = ctypes.create_string_buffer(lvitem_str)
	copied = ctypes.create_string_buffer(4)
	p_copied = ctypes.addressof(copied)
	WriteProcessMemory(hProcHnd, pLVI, ctypes.addressof(lvitem_buffer), ctypes.sizeof(lvitem_buffer), p_copied)
 
	# iterate items in the SysListView32 control
	num_items = win32gui.SendMessage(hwnd, commctrl.LVM_GETITEMCOUNT)
 
	item_texts = []
	for item_index in range(num_items):
		win32gui.SendMessage(hwnd, commctrl.LVM_GETITEMTEXT, item_index, pLVI)
		target_buff = ctypes.create_string_buffer(4096)
		ReadProcessMemory(hProcHnd, pBuffer, ctypes.addressof(target_buff), 4096, p_copied)
		item_texts.append(target_buff.value)
 
	VirtualFreeEx(hProcHnd, pBuffer, 0, MEM_RELEASE)
	VirtualFreeEx(hProcHnd, pLVI, 0, MEM_RELEASE)
	win32api.CloseHandle(hProcHnd)
	return item_texts