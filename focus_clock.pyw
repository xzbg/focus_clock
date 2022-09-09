#!/usr/bin/python3
# author: shenhj
# Filename: focus_clock.py
from src import clock_view
import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) >= 3:
        clock_view.T_FOCUS_TIME = int(args[1])
        clock_view.T_FREE_TIME = int(args[2])
    view = clock_view.ClockView()
    view.geometry()
    view.show()
