__author__ = 'rekhin'
#!/usr/bin/python
import os
from subprocess import call
import pexpect
DEVICE_ID = '954d0ac'
def getDeviceState():
    device = " ".join(os.popen('adb -s '+DEVICE_ID+' get-state').readlines())
    call("ls",shell=True)
    print device


def main():
    getDeviceState()
    device = " ".join(os.popen('adb -s '+DEVICE_ID+' get-state').readlines())
    os.system("ls" , shell=True)
    print device
    main()