#!/bin/bash
export DISPLAY="unix$DISPLAY"
xhost +si:localuser:root
/usr/bin/python3 /home/kirbypi/piscale2/work_tmp/scale_gui.py
