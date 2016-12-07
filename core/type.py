# -*- coding: utf-8 -*-

class board():
    def __init__(self):
        self.plate = []
    
    def input(self, board):
        data = board.split('\n')
        del data[0]
        self.plate = data
        self.analysis()
    
    def analysis(self):
        self.row = len(self.plate)
        self.col = len(self.plate[0])
        print('row', self.row)
        print('col', self.col)

class leader():
    def __init__(self):
        self.set()
    
    def set(self, color=[], combo=0, conection=3, orbConection=3):
        self.color = color
        self.combo = combo
        self.conection = conection
        self.orbConection = orbConection

class route():
    def __init__(self):
        self.list = []
    
    def go(self, direction):
        self.list += direction
