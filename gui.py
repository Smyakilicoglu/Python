# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:46:45 2023

@author: Sümeyra KILIÇOĞLU
"""

import pyautogui
for i in range(10): #Move mouse in a squites
    pyautogui.moveTo(100, 100, duration =0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duratione=0.25)
    pyautogui.moveTo(100, 200, duration =0.25)

wh = pyautogui.size()

#wh.width genişlik öğrenmek için kullanılır.