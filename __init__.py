import sys
import os
import shutil
from cudatext import *
from . import format_proc

if os.name=='nt':
    from . import pyastyle
else:
    try:
        import pyastyle
    except:
        pyastyle = None
        msg_box('For "AStyle Format" plugin, you need to install "pyastyle" Python module in OS. Run:\nsudo pip3 install pyastyle',
            MB_OK+MB_ICONERROR)


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
