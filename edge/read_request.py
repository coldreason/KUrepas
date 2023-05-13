def get_taskIDs_with_unitID_zero(requestQueue):
    taskIDs = []
    for item in requestQueue:
        if item['unitID'] == 0:
            taskIDs.append(item['taskID'])
    return taskIDs

def get_taskIDs_with_unitID_one(requestQueue):
    taskIDs = []
    for item in requestQueue:
        if item['unitID'] == 1:
            taskIDs.append(item['taskID'])
    return taskIDs

def get_taskIDs_with_unitID_two(requestQueue):
    taskIDs = []
    for item in requestQueue:
        if item['unitID'] == 2:
            taskIDs.append(item['taskID'])
    return taskIDs

def get_taskIDs_with_unitID_three(requestQueue):
    taskIDs = []
    for item in requestQueue:
        if item['unitID'] == 3:
            taskIDs.append(item['taskID'])
    return taskIDs

def get_taskIDs_with_unitID_four(requestQueue):
    taskIDs = []
    for item in requestQueue:
        if item['unitID'] == 4:
            taskIDs.append(item['taskID'])
    return taskIDs
