@echo off
setlocal EnableDelayedExpansion
cd /d %~dp0%
python focus_clock.pyw 30 5
exit