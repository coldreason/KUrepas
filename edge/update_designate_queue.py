def write_designateQueue(writeData, designateQueue):
    print('designate updated')
    print(writeData['complete'])  
    taskID = writeData['taskID']
    unitID = writeData['unitID']
    
    if taskID == designateQueue['taskID'] and unitID == designateQueue['unitID']:
        writeData['complete'] = 1
    
    object_out = json.dumps(writeData)
    connection_out(object_out)
    return 0
