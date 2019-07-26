import math

framePositions = []
finalPositions = []

IDnum = 0
movementThresh = 20

currentAnt = {
    'id'          : 0,
    'orientation' : 0, 
    'position'    : (0, 0)
    }

frameNum = 0

def expandFrames():
    for i in range(0, 150): #number of frames
        finalPositions.append([])
    
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0]) **2 + (p0[1] - p1[1])**2)

def orientation(p0, p1):
    return math.degrees(math.atan((p1[1] - p0[1]) / (p0[0] - p1[0])))

def getID(pos, frameNumber):#add object check later
    if len(framePositions) == 0:
        currentAnt['id'] = IDnum
        IDnum += 1
    else:
        for i, previousPosition in finalPositions[frameNumber-1]:
            distances.append(distance(pos, previousPosition[1]))
            minDist = min(distances)
            if minDist < 20:
                currentAnt['id'] = finalPositions[frameNumber-1][i][0]
            else:
                currentAnt['id'] = IDnum
                IDnum += 1
            
def getOrientation(pos, frameNumber)
