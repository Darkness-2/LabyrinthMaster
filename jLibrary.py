#-------------------------------------------------------------------------------
# Name:        jLibrary
# Purpose:     A group of functions I like to use.
#
# Author:      Justin Moulton
#
# Created:     October 10, 2012
# Updated:     February 11, 2013
# Copyright:   (c) Justin Moulton 2013
# Licence:     This work is licensed under the Creative Commons
#              Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#              To view a copy of this license, visit
#              http://creativecommons.org/licenses/by-nc-sa/3.0/.
#-------------------------------------------------------------------------------

version = 0.10 # Version number

def printVersion(): # Function to check the version of jModule being used
    print 'jLibrary',
    print version,
    print 'installed.'

def getPositiveInt(message): # Function to get positive integer input
    userInput = raw_input(message) # Get the user input
    if userInput.isdigit() == False: # If it is not an integer,
        print 'Please enter a positive integer!'
        userInput = getPositiveInt(message) # then get the user to try again
    elif int(userInput) <= 0: # Else if the user input is less than or equal to zero,
        print 'Please enter a positive integer!'
        userInput = getPositiveInt(message) # then get the user to try again
    return int(userInput) # After checking and re-checking, return the user input

def getStrInput(message): # Function to get string input
    userInput = raw_input(message) # Get user input
    return userInput # Return the user input

def getAnyInt(message): # Function to get any integer input
    userInput = raw_input(message) # Get user input
    try: # Try to convert it to an integer
        int(userInput)
    except ValueError: # If conversion is not possible, get the user to try again
        print 'Please enter an integer!'
        userInput = getAnyInt(message)
    return int(userInput) # After checking and re-checking, return the user input

def getFloatInput(message): # Function to get float input
    userInput = raw_input(message) # Get the user input
    try: # Try to convert it to a float
        float(userInput)
    except ValueError: # If conversion is not possible, get the user to try again
        print 'Please enter a number!'
        userInput = getFloatInput(message)
    return float(userInput) # After checking and re-checking, return the user input

def getZeroInt(message): # Function to get integer input that is greater than or equal to zero
    userInput = raw_input(message) # Get the user input
    if userInput.isdigit() == False: # If it is not an integer,
        print 'Please enter an integer greater than or equal to zero!'
        userInput = getZeroInt(message) # then get the user to try again
    elif int(userInput) < 0: # Else if the user input is less than zero,
        print 'Please enter an integer greater than or equal to zero!'
        userInput = getZeroInt(message) # then get the user to try again
    return int(userInput) # After checking and re-checking, return the user input

def getYesNoInput(message): # Function to get yes or no input
    userInput = raw_input(message) # Get the user input
    userInput = userInput.lower()
    if not(userInput == 'y' or userInput == 'Y' or userInput == 'Yes' or userInput == 'yes' or userInput == 'YES' or userInput == 'n' or userInput == 'N' or userInput == 'No' or userInput == 'no' or userInput == 'NO'): # If the userInput is not yes or no,
        print 'Please enter either yes or no!'
        userInput = getYesNoInput(message) # then get them to try again
    if userInput == 'y' or userInput == 'Y' or userInput == 'Yes' or userInput == 'yes' or userInput == 'YES' or userInput == 1: # If the user input is yes,
        return True # then return true
    else: # Else,
        return False # return false

def getOption(message, low, high): # Function to get user option input
    userInput = raw_input(message) # Get the user input
    if userInput.isdigit() == False: # If it is not an integer,
        print 'Please enter a choice between {0} and {1}!'.format(low, high)
        userInput = getOption(message, low, high) # then get the user to try again
    elif int(userInput) < low or int(userInput) > high: # Else if the user input is not within the option range,
        print 'Please enter a choice between {0} and {1}!'.format(low, high)
        userInput = getOption(message, low, high) # then get the user to try again
    return int(userInput) # After checking and re-checking, return the user input

def bubbleSort(array): # Function to bubble sort an array of data
    counter = 0 # Create the required variables
    switch = 0
    while counter < len(array) - 1 or switch == 1: # Start the main sorting loop
        if counter == len(array) - 1: # If the length of the array minus one is equal to counter, start the process over again
            counter = 0
            switch = 0
        if array[counter] > array[counter + 1]: # If the first index is bigger than the second, switch them
            temp = array[counter]
            array[counter] = array[counter + 1]
            array[counter + 1] = temp
            switch = 1 # Set switch to one
        counter += 1 # Increment the counter
    return array # Return the sorted array

def shellSort(array): # Function to shell sort an array
    counter = 0 # Create the required variables
    while counter < len(array): # While the counter is less than the length of the array,
        counterTwo = 0 # Create the required variables
        while counterTwo < len(array): # While the second counter is less than the length of the array,
            if array[counterTwo] > array[counter]: # If the second index is greater than the first index, switch them
                temp = array[counterTwo]
                array[counterTwo] = array[counter]
                array[counter] = temp
            counterTwo += 1 # Increment the second counter
        counter += 1 # Increment the first counter
    return array # Return the sorted array

def insertionSort(array): # Function to insertion sort an array
    counter = 0 # Create the required variables
    newArray = []
    smallest = array[counter]
    originalLength = len(array)
    while len(newArray) < originalLength: # While the new array's length is less than the original length,
        while counter < len(array): # While the counter is less than the length of the array,
            if smallest >= array[counter]: # If the array[counter] is smaller than the current smallest,
                smallest = array[counter] # Set the new smallest
                smallestIndex = counter # Set the smallest's index
            counter += 1 # Increment the counter
        counter = 0 # Reset the counter
        newArray.append(smallest) # Append the new array with the smallest
        array.pop(smallestIndex) # Remove the smallest item from the array
        if len(array) > 0: # If the length of the array is over 0,
            smallest = array[0] # Get the new starting point
    return newArray # Return the new array

def printWithSpacing(toPrint, spacing, newLine): # Function to print with spacing
    if newLine: # If newLine is true,
        print toPrint, # Print the message
        print ' ' * (spacing - len(toPrint)) # Print the spaces with a new line
    else: # Else,
        print toPrint, # Print the message
        print ' ' * (spacing - len(toPrint)), # Print the spaces without a new line