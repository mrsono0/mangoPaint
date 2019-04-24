# coding: utf-8
# python3.5.3
# main.py


import os
import sys
import traceback

from mangopaint import MangoPaint

try:
    import kivy
    kivy.require('1.9.1')
except Exception:
    directory = os.path.split(os.path.abspath(sys.argv[0]))[0]
    traceback.print_exc(file=open('{}/error.log'.format(directory), 'w'))


__version__ = "0.0.1"


# return 은 mangopaint.py 에서.
class main():
    app = None
    app = MangoPaint()
    # laod_ads(app)
    app.run()


if __name__ in ('__main__', '__android__'):
    main()
