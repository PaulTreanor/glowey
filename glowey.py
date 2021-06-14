#!/usr/bin/env python3

import os
import json_methods 
import subprocess
import sys

MIN_VALUE, MAX_VALUE = 0.1, 1.1 # min is 0.1 to avoid making screens unreadble for people

def getOutputID():
    queryOutput = subprocess.check_output("xrandr -q", shell=True).decode(sys.stdout.encoding).strip()

    queryOutput = queryOutput.split(" ")        # list of words 

    # Get string before "connected"
    i = 0
    while i < len(queryOutput):
        if queryOutput[i] == "connected":
            outputItem = queryOutput[i-1]
        i += 1 

    # seperate into words 
    outputItem = outputItem.split("\n")
    outputItem = outputItem[-1]        
    return outputItem      



def changeValues(input):
    json_values = json_methods.readJSON()

    json_values['output'] = getOutputID()
    
    # update the values 
    if input == "up":
        json_values['brightness'] += 0.1
        json_values['temperature'] += 0.05
    if input == "down":
        json_values['brightness'] -= 0.1
        json_values['temperature'] -= 0.05

    # If values outside of min max thresholds don't do anything
    if not MIN_VALUE <= json_values['brightness'] < MAX_VALUE: 
        return 

    # write to json 
    json_methods.writeJSON(json_values)  


def runCommand():                      # Read JSON and run shell command to adjust screen
    config = json_methods.readJSON()
    brightness = config['brightness']
    temperature = config['temperature']
    output = config['output']

    command = "xrandr --output {} --gamma 1:1:{} --brightness {}".format(output, temperature, brightness)
    os.system(command)


def validateArgs(args):
    known_arguments = ["up", "down", "help", "day", "night"]

    if len(args) != 2:
        print("Error, wrong number of args")
        sys.exit()

    if args[1] not in known_arguments:
        print("Argument not known")
        sys.exit()


def help():
    print("Usage: glowey.py <argument>")
    print("Valid arguments are:\n   - up\n   - down\n   - help\n   - day\n   - night\n")


def main(args): 

    # validate args
    validateArgs(args)

    instr = args[1]

    if instr == "help":
        help()

    elif instr in ["day", "night"]:
        print("Sorry this method hasn't been implemented yet.")

    else:
        # set brightness/temperature
        changeValues(instr)

        # Run command 
        runCommand()



if __name__ == "__main__":
    main(sys.argv)
    

"""TODO:
        - Add -day and -night presets
        - Help screen 
        - Similar commands with errors  
""" 