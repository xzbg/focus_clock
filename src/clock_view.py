#!/usr/bin/python3
# author: shenhj
# Filename: clock_view.py
# 计时器界面
from tkinter import *
from src.clock import *

STATUS_WAIT = 0
STATUS_LOOP = 1
STATUS_PAUSE = 2

C_FOCUS_COLOR = '#EDACA7'
C_FREE_COLOR = '#97C18D'

T_FOCUS_TIME = 25
T_FREE_TIME = 5

STR_TITLE = "专注时钟"
STR_FOCUS = "专心干活"
STR_FREE = "休息一下"
STR_START = "开始"
STR_RESUME = "恢复"
STR_PAUSE = "暂停"
STR_FONT = "黑体"


class ClockView:

    def __init__(self):
        self.status = STATUS_WAIT
        self.is_focus = False
        self.clock = Clock()
        self.view = Tk()
        self.view.title(STR_TITLE)
        self.view.attributes('-topmost', True)
        self.lab_text = StringVar()
        self.lab_text.set(f"{str(T_FOCUS_TIME).zfill(2)}:00")
        self.btn_text = StringVar()
        self.btn_text.set(STR_START)
        self.lab = Label(self.view, textvariable=self.lab_text, font=(STR_FONT, 50))
        self.lab.pack(side=TOP)
        self.btn = Button(self.view, textvariable=self.btn_text, font=(STR_FONT, 22), command=self.on_action)
        self.btn.pack(side=BOTTOM)

    def geometry(self, width=300, height=120):
        screen_width = self.view.winfo_screenwidth()
        screen_height = self.view.winfo_screenheight()
        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)
        self.view.geometry(f'{width}x{height}+{x}+{y}')
        self.view.resizable(False, False)

    def show(self):
        self.view.protocol('WM_DELETE_WINDOW', self.on_quit)
        self.view.mainloop()

    def on_quit(self):
        self.clock.stop()
        self.view.quit()

    def on_action(self):
        if self.status == STATUS_WAIT:
            self.on_start(T_FOCUS_TIME, True)
        elif self.status == STATUS_PAUSE:
            self.on_resume()
        else:
            self.on_pause()

    def on_start(self, time, focus):
        self.status = STATUS_LOOP
        self.view.attributes('-topmost', True)
        self.lab_text.set(f"{str(time).zfill(2)}:00")
        self.is_focus = focus
        self.set_focus()
        self.clock.start(duration=time, update_call=self.on_update, cancel_call=self.on_cancel)

    def on_resume(self):
        self.status = STATUS_LOOP
        self.set_focus()
        self.view.attributes('-topmost', True)
        self.clock.resume()

    def on_pause(self):
        self.btn_text.set(STR_RESUME)
        self.status = STATUS_PAUSE
        self.set_color('#F0F0F0')
        self.view.attributes('-topmost', False)
        self.clock.pause()

    def on_update(self, x, y):
        self.lab_text.set(f"{str(x).zfill(2)}:{str(y).zfill(2)}")

    def on_cancel(self):
        if self.is_focus:
            self.on_start(T_FREE_TIME, False)
        else:
            self.on_start(T_FOCUS_TIME, True)

    def set_focus(self):
        if self.is_focus:
            self.btn_text.set(STR_FOCUS)
            self.set_color(C_FOCUS_COLOR)
        else:
            self.btn_text.set(STR_FREE)
            self.set_color(C_FREE_COLOR)

    def set_color(self, color):
        self.view.config(background=color)
        self.lab.config(background=color)
        self.btn.config(background=color)
