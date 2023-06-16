#ListView Control 찾아 조정하는 역할

# -*- coding: utf-8
import win32gui
import pywintypes
from listview_peek import ListViewPeek
 
 
class ControlPicker:
    def __init__(self, parent_window_name):
        self.parent_window_handle = 0
        self.child_windows = []
 
        try:
            win32gui.EnumWindows(self.__enum_window_handler, parent_window_name)
        except pywintypes.error as e:
            if e[0] == 0:
                pass
 
        win32gui.EnumChildWindows(self.parent_window_handle, self.__enum_child_window_handler, None)
 
    def __enum_window_handler(self, window_handle, extra):
        window_text = win32gui.GetWindowText(window_handle)
        if window_text.find(extra) != -1:
            self.parent_window_handle = window_handle
            return pywintypes.FALSE  # stop enumerating
 
    def __enum_child_window_handler(self, window_handle, extra):
        self.child_windows.append(window_handle)
 
    def pick_control(self, target_class_name, target_control_id = None):
        for child_window in self.child_windows:
            window_class = win32gui.GetClassName(child_window)
            control_id = win32gui.GetDlgCtrlID(child_window)
 
            if window_class != target_class_name:
                continue
 
            if target_control_id:
                if target_control_id == control_id:
                    return child_window
            else:
                return child_window
 
 
if __name__ == '__main__':
    import sys
    import time
 
    picker = ControlPicker('SubRenamer')
    list_view_control = picker.pick_control('SysListView32', 0x3EC)
    if not list_view_control:
        print "SysListView32 not found!"
        sys.exit(1)
 
    peek = ListViewPeek(list_view_control)
 
    print "There are %d items in the ListView control!" % (peek.get_item_count(), )
    for x in peek.get_list_items():
        print x
    print
 
    if peek.get_item_count() < 2:
        print "Make sure Subrenamer has enough unmatched video lists!"
        sys.exit(1)
 
    pause = 5
    win32gui.SetActiveWindow(picker.parent_window_handle)
    win32gui.SetForegroundWindow(list_view_control)
    print "Target window is selected. %d seconds sleep..." % (pause, )
    time.sleep(pause)
 
    peek.select_item(-1, False)
    print "No item selected. %d seconds sleep..." % (pause, )
    time.sleep(pause)
 
    peek.select_item(0, True)
    print "The first item selected. %d seconds sleep..." % (pause, )
    time.sleep(pause)
 
    peek.select_item(-1, False)
    peek.select_item(1, True)
    print "The second item selected. %d seconds sleep..." % (pause, )
    time.sleep(pause)
 
    peek.select_item(-1, True)
    print "All selected. %d seconds sleep..." % (pause, )
    time.sleep(pause)
 
    peek.select_item(-1, False)
    print "None selected again."
    print "Done!"