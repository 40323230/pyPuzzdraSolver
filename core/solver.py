# -*- coding: utf-8 -*-
from .type import board, route, leader

class OrbRule():
    def __init__(self):
        ''''''
    
    def cleanUp(self, board, leader):
        orbConection = leader.orbConection
        #Horizontal
        plateH = board.plate
        for row in plateH:
            for col in row:
                handleType = col
                if handleType=='X': continue
                preorb = 0
                nextorb =0
                preType1 = row[col-1] if row.index(col)!=0 else 'X'
                preType2 = row[col-2] if row.index(col)!=0 else 'X'
                nextType1 = row[col+1] if row.index(col)<=len(row) else 'X'
                nextType2 = row[col+2] if row.index(col)<=len(row) else 'X'
        #Vertical
        plateV = board.plate
        #Compare
        

class combo():
    def __init__(self):
        self.conection = 0
        
