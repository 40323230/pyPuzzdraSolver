# -*- coding: utf-8 -*-

from sys import argv
from core.main import Operator

if __name__=='__main__':
    if len(argv)<2 or not('.txt' in argv): print('Please input files.')
    else:
        result = Operator()
