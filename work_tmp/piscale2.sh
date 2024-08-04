/home/kirbypi/venv/bin/python3#!/bin/bash
export DISPLAY="unix$DISPLAY"
xhost +si:localuser:root
/home/kirbypi/piscale2/venv/bin/python /home/kirbypi/piscale2/work_tmp/scale_gui.py
