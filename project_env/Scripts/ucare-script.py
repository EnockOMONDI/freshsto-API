#!"c:\users\hp 440 g3\desktop\apps\projects\yumi-1.1\project_env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'pyuploadcare==2.6.0','console_scripts','ucare'
__requires__ = 'pyuploadcare==2.6.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyuploadcare==2.6.0', 'console_scripts', 'ucare')()
    )
