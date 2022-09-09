#!/usr/bin/python3
# author: shenhj
# Filename: clock.py
# 时钟
from threading import Timer
import math


class Clock:
    def __init__(self):
        """
        初始化计时器
        """
        self.status = False
        self.minute = 0
        self.second = 0
        self.update_call = None
        self.cancel_call = None
        self.duration = 0
        self.timer: Timer = None

    def __del__(self):
        if self.timer is not None:
            self.timer.cancel()
            self.timer = None

    def start(self, duration=25, update_call=None, cancel_call=None):
        """
        启动计时器
        :return:
        """
        self.minute = duration
        self.second = duration * 60
        self.update_call = update_call
        self.cancel_call = cancel_call
        self.duration = 0
        self.status = True
        self.timer = Timer(1, self.update)
        self.timer.start()

    def stop(self):
        """
        停止计时器
        :return:
        """
        if self.timer is not None:
            self.timer.cancel()

    def pause(self):
        self.status = False

    def resume(self):
        self.status = True
        self.update()

    def update(self):
        """
        计时器更新
        :return:
        """
        if not self.status:
            return
        minute = self.second - self.duration
        second = math.fmod(self.second - self.duration, 60)
        if self.duration >= self.second:
            if self.cancel_call is not None:
                self.timer.cancel()
                self.cancel_call()
        else:
            self.duration += 1
            if self.update_call is not None:
                self.update_call(int(minute / 60), int(second))
            self.timer = Timer(1, self.update)
            self.timer.start()
