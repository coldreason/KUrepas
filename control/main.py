from decoder import *
from encoder import *

taskSet = [[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
           [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
           [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0]],
           [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
           [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]]

for i in range(0, 5) :
    encoder_taskSet(taskSet[i])

while True:
    taskQueueData = decoder_taskQueue() # [pos_x, pos_y]
    scoreQueueData = decoder_scoreQueue()
    designateQueueData = decoder_designateQueue()
    if(taskQueueData != None) :
        for i in range(0, 5) :
            if taskSet[i][taskQueueData['pos_s_x']][taskQueueData['pos_s_y']] == 1:
                encoder_requestQueue({'unitID' : i, 'taskID' : taskQueueData['taskID']})
        print('new taskQueue exists')
    if(scoreQueueData != None) :
        print('new scoreQueue exists')
    if(designateQueueData != None) :
        print('new designateQueue exists')