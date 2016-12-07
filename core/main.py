# -*- coding: utf-8 -*-
from .type import board, leader
from .result import result

class Operator():
    def __init__(self):
        self.originBoard = board()
        self.originBoard.input(testBoard())
        self.leaderRequire = leader()
        self.results = []

def testBoard():
    return """
123456
111111
111111
111111
111111"""
