import os
import sys

extension = '.jpg'

for arg in sys.argv[1:]:
    os.rename(arg, arg + extension)
