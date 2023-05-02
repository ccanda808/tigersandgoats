'''
Huligutta (Goats and Tigers)
file: game.py
Description: GUI of the game using TKinter
'''

__author__ = "Cameron Canda and group"
__status__ = "Dev"

import numpy as np
from huligutta import *
from functions import *

def generateState(numOfGoats):
    
    state = {'b0': (),'a1': (),'a2': (),'a3': (),
        'b1': (),'b2': (),'b3': (),'b4': (),
        'c1': (),'c2': (),'c3': (),'c4': (),
        'd1': (),'d2': (),'d3': (),'d4': (),
        'e1': (),'e2': (),'e3': (),'e4': (),
        'f1': (),'f2': (),'f3': ()}
    
    board = ['b0','a1','a2','a3',
        'b1','b2','b3','b4',
        'c1','c2','c3','c4',
        'd1','d2','d3','d4',
        'e1','e2','e3','e4',
        'f1','f2','f3']
    
    positions = np.random.choice(23, numOfGoats+3, replace=False)
    
    for tigers in range(0,3):
        state[board[positions[tigers]]] = 'X'
    for goats in range(3,numOfGoats+3):
        state[board[positions[goats]]] = 'O'
    
    return state

def valueOfPosition(givenBoard, goatEaten, params):
    #return random.random()

    placedGoats = len(goatPositions(givenBoard)) + goatEaten
    #         print(givenBoard)
    #         print(goatPositions(givenBoard))
    #         print(placedGoats)
    if placedGoats == 0:
        return
    goatCountMultiplier = params[0]
    tigerCountMultiplier = params[1]
    badTigerCountMultiplier = params[2]
    weight = params[3]

    # Mobility Value
    tigerPos = tigerPositions(givenBoard)
    mobilityval = 0
    for tiger in tigerPositions(givenBoard):
        for neighbor in Position(tiger[0],tiger[1]).get_neighbors():
            if givenBoard[neighbor] == ():
                mobilityval += 1

    # Safety Value (WIP)
    goatPos = goatPositions(givenBoard)
    safetyval = 0
    for goat in goatPos:
        goatCount = 0
        tigerCount = 0
        badTigerCount = 0
        for neighbor in Position(goat[0],goat[1]).get_neighbors():
            if givenBoard[neighbor] == 'O':
                goatCount = goatCount + 1
            elif givenBoard[neighbor] == 'X':
                if Position(neighbor[0],neighbor[1]).get_captures() == goat:
                    badTigerCount = badTigerCount + 1
                else:
                    tigerCount = tigerCount + 1
        safetyval = safetyval + checkValue(goatCount,tigerCount,badTigerCount,goatCountMultiplier,tigerCountMultiplier,badTigerCountMultiplier)
    maxmobilityval = 4
    maxsafetyval = 4*goatCountMultiplier
    avgsafetyval = safetyval/placedGoats
    avgmobilityval = mobilityval/3
    if goatEaten == 5:
        winprob = 0
    elif len(Piece(tiger).possibleMoves()) == 0:
        winprob = 1
    else:
        winprob = (weight)*(avgsafetyval/maxsafetyval)+(1-weight)*(1-(avgmobilityval/maxmobilityval))
    #print(winprob)
    return winprob

def checkValue(goatCount,tigerCount,badTigerCount,goatCountMultiplier,tigerCountMultiplier,badTigerCountMultiplier):
    return goatCount*goatCountMultiplier + tigerCount*tigerCountMultiplier + badTigerCount*badTigerCountMultiplier

for i in range(1):
    params = [2,-1,-1,0.5]
    goatsEaten = np.random.randint(0,3)
    randState = generateState(12)
    value = valueOfPosition(randState,goatsEaten,params)
    print(params,goatsEaten,randState,value,sep="\n")
