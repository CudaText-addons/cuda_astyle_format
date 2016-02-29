from cudatext import *
import sys
import os
import shutil

if os.name!='nt':
    msg_box('Plugin supports Win32 only', MB_OK)
    raise Exception('')
    
from . import pyastyle
from . import format_proc

format_proc.INI = 'cuda_astyle_format.cfg'
format_proc.MSG = '[AStyle Format] '

def options():
    ini = format_proc.ini_filename()
    if os.path.isfile(ini):
        s = open(ini).read()
    else:
        s = ''
    return s

def do_format(text):
    opt = options()
    #print('AStyle options:', opt)
    return pyastyle.format(text, opt)

class Command:
    def config_global(self):
        format_proc.config_global()

    def config_local(self):
        format_proc.config_local()

    def run(self):
        format_proc.run(do_format)
