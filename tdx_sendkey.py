#!/usr/bin/python
#-*- encoding: gbk -*- 

import ctypes
import win32gui
import win32con
import macro,SendKeys
import os,time,re,sys 
import zipfile,datetime

############################################################
#��ȡ��ǰ����Title
############################################################
def GetForegroundWindowName():
    hwnd = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(hwnd)



