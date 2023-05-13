def write1_scoreQueue(writeData):

    file_path = "performance_scores1.txt"
    data = {}

    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith("Courier 1 Score:"):
                score = int(line.split(":")[1].strip())

                data["Courier 1 Score"] = score

    with open(writeData, "w") as json_file:
        json.dump(data, json_file)

def write2_scoreQueue(writeData):

    file_path = "performance_scores2.txt"
    data = {}

    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith("Courier 2 Score:"):
                score = int(line.split(":")[1].strip())

                data["Courier21 Score"] = score

    with open(writeData, "w") as json_file:
        json.dump(data, json_file)

def write3_scoreQueue(writeData):

    file_path = "performance_scores3.txt"
    data = {}

    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith("Courier 3 Score:"):
                score = int(line.split(":")[1].strip())

                data["Courier 3 Score"] = score

    with open(writeData, "w") as json_file:
        json.dump(data, json_file)

def write4_scoreQueue(writeData):

    file_path = "performance_scores4.txt"
    data = {}

    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith("Courier 4 Score:"):
                score = int(line.split(":")[1].strip())

                data["Courier 4 Score"] = score

    with open(writeData, "w") as json_file:
        json.dump(data, json_file)

def write5_scoreQueue(writeData):

    file_path = "performance_scores5.txt"
    data = {}

    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith("Courier 5 Score:"):
                score = int(line.split(":")[1].strip())

                data["Courier 5 Score"] = score

    with open(writeData, "w") as json_file:
        json.dump(data, json_file)
