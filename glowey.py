#!/usr/bin/python3
import os
import json

MIN_VALUE, MAX_VALUE = 0.1, 1

def readJSON():
    with open('config.json') as configFile:
        config = json.load(configFile)
    return config


def writeJSON(updated_values):
    print(updated_values)
    with open('config.json', 'w') as configFile:
        json.dump(updated_values, configFile)


def changeValues(input):
   old_values = readJSON()

    if input == "up":
        old_values['brightness'] += 0.1
    else:
        old_values['brightness'] -= 0.1

    # If values outside of min max thresholds don't do anything
    if old_values['brightness'] in [0, 1.1]:       # min is 0.1 to avoid making screens unreadble for people
        return none 

    # write to json 
    writeJSON(old_values)       # old values have now been updated 

    # run command 



def main():

    # Get input ("up", "down")

    instr = input("'up' or 'down'")

    changeValues(instr)



    # Run command 

    config = readJSON()
    brightness = config['brightness']
    temperature = config['temperature']
    output = config['output']

    command = "xrandr --output {} --gamma 1:1:{} --brightness {}".format(output, temperature, brightness)
    os.system(command)



if __name__ == "__main__":
    main()