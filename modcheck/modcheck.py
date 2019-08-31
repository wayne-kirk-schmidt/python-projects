#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Explanation: validates the list of python modules are installed incurrent client distribution

Usage:
    $ python  importcheck [ list ]

Style:
    Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

    @name           importcheck
    @version        1.0.00
    @author-name    Wayne Schmidt
    @author-email   wayne.kirk.schmidt@gmail.com
    @license-name   GNU GPL
    @license-url    http://www.gnu.org/licenses/gpl.html
"""

__version__ = 1.00
__author__ = "Wayne Schmidt (wayne.kirk.schmidt@gmail.com)"

import sys
sys.dont_write_bytecode = 1

COUNT = 0
ISSUE = 0

PIPLIST = list()

MODULES = list()
sys.argv.pop(0)
MODULES = sys.argv

INPUT = str(len(MODULES))

for mymodule in MODULES:
    try:
        globals()[mymodule] = __import__(mymodule)
        COUNT = COUNT + 1
        if not isinstance(locals()[mymodule], type(sys)):
            ISSUE = ISSUE + 1
            PIPLIST.append(mymodule)
    except:
        ISSUE = ISSUE + 1
        PIPLIST.append(mymodule)

print('### Modules-Provided: %s ' % INPUT)
print('### Modules-Imported: %s ' % COUNT)
print('### Modules-Problems: %s ' % ISSUE)

for pipitem in PIPLIST:
    print('### Installation ### sudo -H pip3 install %s ' % pipitem)
