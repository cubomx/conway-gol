

def create_file(filename:str):
    file_ = open(filename, "w")
    return file_


def saveData(step:int, cells:int, file_):
    file_.write('step: ' + str(step) + " cells alive: " + str(cells) + "\n")

def close_file(file_):
    file_.close()
