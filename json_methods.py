import json 

def readJSON():
    with open('config.json') as configFile:
        config = json.load(configFile)
    return config


def writeJSON(updated_values):
    print(updated_values)
    with open('config.json', 'w') as configFile:
        json.dump(updated_values, configFile)