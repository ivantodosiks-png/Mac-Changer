#!/usr/bin/env python

import subprocess

subprocess.call("sudo ip link set eth0 down", shell=True)
subprocess.call("sudo ifconfig eth0 hw ether 02:22:33:44:55:66", shell=True)
subprocess.call("sudo ip link set eth0 up", shell=True)
