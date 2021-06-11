#!/usr/bin/python3
import os
import json

MIN_VALUE, MAX_VALUE = 0.1, 1

def readJSON():
    with open('config.json') as configFile:
        config = json.load(configFile)
    return config


def changeValues(input):
    # readJSON
    # increment value 
    # if values greater than 1 or less than 0
    #   pass
    # config['brightness'] = value
    # config []

    old_values = readJSON()

    if input == "up":
        old_values['brightness'] += 0.1
    else:
        old_values['brightness'] -= 0.1

    if old_value['brightness'] in [0, 1.1]:       # min is 0.1 to avoid making screens unreadble for people
        return none 

    if input = 1



def main():

    # Get input ("up", "down")



    # Change JSON values



    # Run command 

    config = readJSON()
    brightness = config['brightness']
    temperature = config['temperature']
    output = config['output']

    command = "xrandr --output {} --gamma 1:1:{} --brightness {}".format(output, temperature, brightness)
    os.system(command)



if __name__ == "__main__":
    main()