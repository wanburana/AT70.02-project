import os
import json
import time
from configs import *

def save2Json(dict, filename = f"map-{int(time.time())}.json"):
    # not exist and be directory.
    path = os.path.join(MAP_DIRECTORY, filename)
    if not os.path.exists(path) and os.path.dirname(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)

    jsonString = json.dumps(dict)
    jsonFile = open(path, "w")
    jsonFile.write(jsonString)
    jsonFile.close()

def loadJson2Dict(filename):
    path = os.path.join(MAP_DIRECTORY, filename)
    fileObject = open(path, "r")
    jsonContent = fileObject.read()
    return json.loads(jsonContent)