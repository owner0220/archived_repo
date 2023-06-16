# -*- coding: utf-8 -*-
import win32gui
import win32api
import commctrl
import ctypes
from win32con import PAGE_READWRITE, MEM_COMMIT, MEM_RESERVE, MEM_RELEASE, PROCESS_ALL_ACCESS
 
GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId
VirtualAllocEx = ctypes.windll.kernel32.VirtualAllocEx
VirtualFreeEx = ctypes.windll.kernel32.VirtualFreeEx
OpenProcess = ctypes.windll.kernel32.OpenProcess
WriteProcessMemory = ctypes.windll.kernel32.WriteProcessMemory
ReadProcessMemory = ctypes.windll.kernel32.ReadProcessMemory
 
 
class LVItem(ctypes.Structure):
    """
    LVITEM structure: https://msdn.microsoft.com/en-us/library/windows/desktop/bb774760%28v=vs.85%29.aspx
 
       UINT   mask
       int    iItem
       int    iSubItem
       UINT   state
       UINT   stateMask
       LPTSTR pszText
       int    cchTextMax
       int    iImage
       LPARAM lParam
 
    Total 9 items
    """
    _fields_ = [
        ("mask", ctypes.c_uint),
        ("iItem", ctypes.c_int),
        ("iSubItem", ctypes.c_int),
        ("state", ctypes.c_uint),
        ("stateMask", ctypes.c_uint),
        ("pszText", ctypes.c_char_p),
        ("cchTextMax", ctypes.c_int),
        ("iImage", ctypes.c_int),
        ("lParam", ctypes.c_ulong),
    ]
 
 
class ListViewPeek(object):
 
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.pid = ctypes.c_uint()
 
        GetWindowThreadProcessId(self.hwnd, ctypes.addressof(self.pid))
        self.process_handle = OpenProcess(PROCESS_ALL_ACCESS, False, self.pid)
        self.p_lvi = VirtualAllocEx(self.process_handle, 0, 4096, MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE)
        self.p_buf = VirtualAllocEx(self.process_handle, 0, 4096, MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE)
 
    def __del__(self):
        VirtualFreeEx(self.process_handle, self.p_buf, 0, MEM_RELEASE)
        VirtualFreeEx(self.process_handle, self.p_lvi, 0, MEM_RELEASE)
        win32api.CloseHandle(self.process_handle)
 
    def get_item_count(self):
        return win32gui.SendMessage(self.hwnd, commctrl.LVM_GETITEMCOUNT)
 
    def get_list_items(self):
        init_list = [0, 0, 0, 0, 0, self.p_buf, 4096, 0, 0]
        self.init_p_lvi(init_list)
 
        num_items = self.get_item_count()
        items = []
        extraction_buffer = ctypes.create_string_buffer(4096)
 
        for i in xrange(num_items):
            win32gui.SendMessage(self.hwnd, commctrl.LVM_GETITEMTEXT, i, self.p_lvi)
            self.__read_from_buffer(self.p_buf, ctypes.addressof(extraction_buffer), ctypes.sizeof(extraction_buffer))
            items.append(extraction_buffer.value)
        return items
 
    def select_item(self, index, selected):
        """
        index:     zero-based item index. -1 for select all.
        selected:  set True/False to select/deselect.
        """
        lv_item_list = [
            commctrl.LVIF_STATE,
            0,
            0,
            commctrl.LVIS_SELECTED if selected else 0,
            commctrl.LVIS_SELECTED,
            0,
            0,
            0,
            0,
        ]
        self.init_p_lvi(lv_item_list)
        return win32gui.SendMessage(self.hwnd, commctrl.LVM_SETITEMSTATE, index, self.p_lvi)
 
    def init_p_lvi(self, init_list):
        lv_item_buf = LVItem(*init_list)
        return self.__write_to_buffer(self.p_lvi, ctypes.byref(lv_item_buf), ctypes.sizeof(lv_item_buf))
 
    def __write_to_buffer(self, source, destination, read_size):
        copied = ctypes.c_uint()
        p_copied = ctypes.addressof(copied)
        WriteProcessMemory(self.process_handle, source, destination, read_size, p_copied)
        return copied.value
 
    def __read_from_buffer(self, source, destination, read_size):
        copied = ctypes.c_uint()
        p_copied = ctypes.addressof(copied)
        ReadProcessMemory(self.process_handle, source, destination, read_size, p_copied)
        return copied.value