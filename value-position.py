'''
Huligutta (Goats and Tigers)
file: game.py
Description: GUI of the game using TKinter
'''

__author__ = "Cameron Canda and group"
__status__ = "Dev"

params = [2,-1,-1,0.5]

def valueOfPosition(self, givenBoard, goatEaten, params):
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
        safetyval = safetyval + self.checkValue(goatCount,tigerCount,badTigerCount,goatCountMultiplier,tigerCountMultiplier,badTigerCountMultiplier)
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

def checkValue(self,goatCount,tigerCount,badTigerCount,goatCountMultiplier,tigerCountMultiplier,badTigerCountMultiplier):
    return goatCount*goatCountMultiplier + tigerCount*tigerCountMultiplier + badTigerCount*badTigerCountMultiplier