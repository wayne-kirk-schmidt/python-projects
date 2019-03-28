#!/usr/bin/env python

""" Simple script to evaluate dependencies and emits required pip modules to install """

__author__ = 'wayne.kirk.schmidt@gmail.com'
__version__ = '1.0.0'

import sys

MODULE_COUNT = 0
IMPORT_ISSUE = 0
MODULE_LISTS = []
MODULE_ISSUE = []
PIP_CMDS = ['pip', 'pip3']

sys.argv.pop(0)
MODULE_LISTS = sys.argv

for MYMODULE in MODULE_LISTS:
    try:
        globals()[MYMODULE] = __import__(MYMODULE)
        if isinstance(locals()[MYMODULE], type(sys)) and not MYMODULE.startswith('__'):
            MODULE_COUNT = MODULE_COUNT + 1
            MODULE_STATUS = 'Present'
    except ImportError as my_error:
        IMPORT_ISSUE = IMPORT_ISSUE + 1
        MODULE_ISSUE.append(MYMODULE)
        MODULE_STATUS = 'Absent'

print 'Requested: {0:3}'.format(str(len(MODULE_LISTS)))
print 'Available: {0:3}'.format(str(MODULE_COUNT))
print 'HaveIssue: {0:3}'.format(str(IMPORT_ISSUE))

if MODULE_ISSUE:
    for PIPTARGET in MODULE_ISSUE:
        for PIPCMD in PIP_CMDS:
            print '\t### {} install {}'.format(PIPCMD, PIPTARGET)
