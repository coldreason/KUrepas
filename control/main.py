from modulescheduling import *

taskQueue2requestQueue()
scoreQueue2designateQueue()
reAllocating()

designateQueueData = decoder_designateQueue()
if(designateQueueData != None) :
	print('new designateQueue exists')