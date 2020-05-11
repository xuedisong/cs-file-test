import sys
import os

if __package__ == '':
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)
    del path

import sxautest.sxau.cs.file.man.provider.user_control as controller

print controller.login()
