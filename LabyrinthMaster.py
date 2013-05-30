#-------------------------------------------------------------------------------
# Name:        LabyrinthMaster
# Purpose:     Main file of LabyrinthMaster.
#
# Author:      Justin Moulton
#
# Created:     May 24, 2013
# Copyright:   (c) Justin Moulton 2013
# Licence:     This work is licensed under the Creative Commons
#              Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#              To view a copy of this license, visit
#              http://creativecommons.org/licenses/by-nc-sa/3.0/.
#-------------------------------------------------------------------------------

import GlobalVars
import pygame
from pygame.locals import *
import sys

def main():
    maps = open('mainMaps.txt') # Open the maps file
    GlobalVars.numLines = sum(1 for line in maps) # Find the number of lines
    maps.seek(0) # Seek the beginning of the file
    pygame.init() # Start pygame
    DISPLAYSURF = pygame.display.set_mode((400, 200)) # Set the pygame display
    pygame.display.set_caption('Labyrinth Master') # Set the caption
    DISPLAYSURF.fill(GlobalVars.black) # Fill the screen black
    GlobalVars.mainFont = pygame.font.Font("freesansbold.ttf", 32) # Initialize the fonts
    GlobalVars.secondaryFont = pygame.font.Font("freesansbold.ttf", 16)
    title = GlobalVars.mainFont.render("Labyrinth Master", 1,  GlobalVars.white) # Create label objects for each line for the title screen
    DISPLAYSURF.blit(title, (62, 10)) # Display each line for the title screen
    lineOne = GlobalVars.secondaryFont.render("Controls: Movement - Arrow Keys", 1, GlobalVars.white)
    DISPLAYSURF.blit(lineOne, (62, 70))
    lineFive = GlobalVars.secondaryFont.render("Reset - R", 1, GlobalVars.white)
    DISPLAYSURF.blit(lineFive, (143, 90))
    lineTwo = GlobalVars.secondaryFont.render("Rules: Collect all keys (yellow)", 1, GlobalVars.white)
    DISPLAYSURF.blit(lineTwo, (62, 120))
    lineThree = GlobalVars.secondaryFont.render("to open the goal(red/green)!", 1, GlobalVars.white)
    DISPLAYSURF.blit(lineThree, (62, 140))
    lineFour = GlobalVars.secondaryFont.render("Press any key to continue...", 1, GlobalVars.white)
    DISPLAYSURF.blit(lineFour, (62, 170))
    pygame.display.update() # Update the display
    keyPressed = False
    while keyPressed == False: # If no key has been pressed,
        for event in pygame.event.get(): # Wait for a key to be pressed
            if event.type == QUIT: # If exit button is hit, quit the game
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN: # If key pressed, exit the loop
                keyPressed = True
    loadNewMap(maps, DISPLAYSURF) # Run the load a new map function
    while True: # Main loop
        if GlobalVars.mapOver == True: # If the map is over,
            GlobalVars.mapOver = False
            movesLine = GlobalVars.secondaryFont.render("Moves: " + str(GlobalVars.moves), 1, GlobalVars.white)
            DISPLAYSURF.fill(GlobalVars.black) # Show the moves taken to complete the map
            DISPLAYSURF.blit(movesLine, (90, 90))
            pygame.display.update() # Update the display and wait 1000ms
            pygame.time.delay(1000)
            loadNewMap(maps, DISPLAYSURF) # Run the load a new map function
        for event in pygame.event.get(): # For an event happening,
            if event.type == QUIT: # If the exit button is hit, quit the game
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN: # If a key is pressed, check the key and run an appropriate function
                if event.key == K_UP:
                    playerMovement('up', DISPLAYSURF) # Run the player movement function for any of the four directions
                    GlobalVars.moves += 1
                elif event.key == K_DOWN:
                    playerMovement('down', DISPLAYSURF)
                    GlobalVars.moves += 1
                elif event.key == K_LEFT:
                    playerMovement('left', DISPLAYSURF)
                    GlobalVars.moves += 1
                elif event.key == K_RIGHT:
                    playerMovement('right', DISPLAYSURF)
                    GlobalVars.moves += 1
                elif event.key == K_r:
                    maps.seek(GlobalVars.mapLinePosition) # If a reset is requested, seek the beginning of the map
                    GlobalVars.mapOver = True # Set map over to true
        pygame.display.update() # Update the display

def playerMovement(direction, DISPLAYSURF): # Function to handle player movement
    goalFound = False
    wallFound = False
    while goalFound == False and wallFound == False: # While a goal or wall has not been found,
        originalXValue = GlobalVars.playerXValue # Store the original X and Y values
        originalYvalue = GlobalVars.playerYValue
        if direction == 'up': # If the direction is up,
            oneUp = [GlobalVars.playerXValue, GlobalVars.playerYValue - 1] # Find the block above the player
            found = False
            counter = 0
            while found == False: # While the block above has not been found, search the array for it
                if GlobalVars.mapArray[counter][:2] == oneUp:
                    found = True
                    nextBlock = GlobalVars.mapArray[counter] # Store the next block
                counter += 1
        elif direction == 'down': # Same as above for any other direction
            oneDown = [GlobalVars.playerXValue, GlobalVars.playerYValue + 1]
            found = False
            counter = 0
            while found == False:
                if GlobalVars.mapArray[counter][:2] == oneDown:
                    found = True
                    nextBlock = GlobalVars.mapArray[counter]
                counter += 1
        elif direction == 'left':
            oneLeft = [GlobalVars.playerXValue - 1, GlobalVars.playerYValue]
            found = False
            counter = 0
            while found == False:
                if GlobalVars.mapArray[counter][:2] == oneLeft:
                    found = True
                    nextBlock = GlobalVars.mapArray[counter]
                counter += 1
        elif direction == 'right':
            oneRight = [GlobalVars.playerXValue + 1, GlobalVars.playerYValue]
            found = False
            counter = 0
            while found == False:
                if GlobalVars.mapArray[counter][:2] == oneRight:
                    found = True
                    nextBlock = GlobalVars.mapArray[counter]
                counter += 1
        if nextBlock[2] == 'w': # If the next block is a wall, set wall found to true
            wallFound = True
        elif nextBlock[2] == 'g': # If the next block is the goal
            GlobalVars.playerXValue = nextBlock[0] # Store the player's X and Y values in the next block
            GlobalVars.playerYValue = nextBlock[1]
            if GlobalVars.playerKeys == GlobalVars.mapKeys: # If all the keys have been found,
                goalFound = True # The goal has been found
                GlobalVars.mapOver = True # The map is over
                pygame.draw.rect(DISPLAYSURF, GlobalVars.yellow, (GlobalVars.playerXValue * 20, GlobalVars.playerYValue * 20, 20, 20))
                pygame.draw.rect(DISPLAYSURF, GlobalVars.gray, (originalXValue * 20, originalYvalue * 20, 20, 20)) # Make the player move onto the goal
                pygame.display.update() # Update the display
            else: # Otherwise, have the player move but do not end the map
                pygame.draw.rect(DISPLAYSURF, GlobalVars.red, (GlobalVars.playerXValue * 20, GlobalVars.playerYValue * 20, 20, 20))
                pygame.draw.rect(DISPLAYSURF, GlobalVars.gray, (originalXValue * 20, originalYvalue * 20, 20, 20))
                pygame.display.update()
                pygame.time.delay(30) # Wait 30ms for animation to show
        elif nextBlock[2] == ' ': # If the next block is open space,
            GlobalVars.playerXValue = nextBlock[0] # Store the player's X and Y values in the next block
            GlobalVars.playerYValue = nextBlock[1]
            pygame.draw.rect(DISPLAYSURF, GlobalVars.blue, (GlobalVars.playerXValue * 20, GlobalVars.playerYValue * 20, 20, 20))
            pygame.draw.rect(DISPLAYSURF, GlobalVars.gray, (originalXValue * 20, originalYvalue * 20, 20, 20)) # Move the player onto the next space
            pygame.display.update() # Update the display
            pygame.time.delay(30) # Wait 30ms for animation to show
        elif nextBlock[2] == 'k': # If the next block is a key,
            GlobalVars.playerXValue = nextBlock[0] # Store the player's X and Y values in the next block
            GlobalVars.playerYValue = nextBlock[1]
            GlobalVars.mapArray[counter - 1] = [nextBlock[0], nextBlock[1], ' '] # Change the key block to be a normal block
            GlobalVars.playerKeys += 1 # Increase the number of player keys
            pygame.draw.rect(DISPLAYSURF, GlobalVars.blue, (GlobalVars.playerXValue * 20, GlobalVars.playerYValue * 20, 20, 20))
            pygame.draw.rect(DISPLAYSURF, GlobalVars.gray, (originalXValue * 20, originalYvalue * 20, 20, 20)) # Move the player onto the key space
            pygame.display.update() # Update the display
            pygame.time.delay(30) # Wait 30ms for animation to show
        if GlobalVars.playerKeys == GlobalVars.mapKeys: # If player keys matches map keys,
                pygame.draw.rect(DISPLAYSURF, GlobalVars.green, (GlobalVars.goalXValue, GlobalVars.goalYValue, 20, 20)) # Open the goal
        else:
                pygame.draw.rect(DISPLAYSURF, GlobalVars.red, (GlobalVars.goalXValue, GlobalVars.goalYValue, 20, 20)) # If not, close it

def loadNewMap(maps, DISPLAYSURF): # Function to load new map
    del GlobalVars.mapArray[:] # Delete the map array
    xValue = 0 # Create all the required variables
    yValue = 0
    GlobalVars.playerKeys = 0
    GlobalVars.mapKeys = 0
    GlobalVars.moves = 0
    lastPos = maps.tell() # Get the file position
    counter = 0
    while counter < GlobalVars.numLines: # While the file is not finished,
        line = maps.readline() # Read a line
        line = line.strip() # Strip the line
        xValue = 0
        if line[0] == 't': # If the next line is a title,
            GlobalVars.mapTitle = "Labyrinth Master - " + line[1:] # Set the caption to the level name
            pygame.display.set_caption(GlobalVars.mapTitle)
            GlobalVars.mapLinePosition = lastPos # Set the map starting position
        elif line[0] == 'l': # If the next line is a level piece,
            line = line[1:] # Strip the beginning
            for letter in line: # For each letter in the line,
                if letter == 'w': # If it's a wall, draw a wall
                    pygame.draw.rect(DISPLAYSURF, GlobalVars.black, (xValue, yValue, 20, 20))
                    GlobalVars.mapArray.append([xValue / 20, yValue / 20, 'w'])
                    xValue += 20
                elif letter == ' ': # If it's open space, draw open space
                    pygame.draw.rect(DISPLAYSURF, GlobalVars.gray, (xValue, yValue, 20, 20))
                    GlobalVars.mapArray.append([xValue / 20, yValue / 20, ' '])
                    xValue += 20
                elif letter == 's': # If it's a starting position, set the player position and draw the player
                    pygame.draw.rect(DISPLAYSURF, GlobalVars.blue, (xValue, yValue, 20, 20))
                    GlobalVars.playerXValue = xValue / 20
                    GlobalVars.playerYValue = yValue / 20
                    GlobalVars.mapArray.append([xValue / 20, yValue / 20, ' '])
                    xValue += 20
                elif letter == 'g': # If it's a goal, set the goal position
                    GlobalVars.goalXValue = xValue
                    GlobalVars.goalYValue = yValue
                    GlobalVars.mapArray.append([xValue / 20, yValue / 20, 'g'])
                    xValue += 20
                elif letter == 'k': # If it's a key, draw a key
                    pygame.draw.rect(DISPLAYSURF, GlobalVars.yellow, (xValue, yValue, 20, 20))
                    GlobalVars.mapArray.append([xValue / 20, yValue / 20, 'k'])
                    GlobalVars.mapKeys += 1
                    xValue += 20
            yValue += 20
        elif line[0] == 'e': # If the line begins with an e,
            if GlobalVars.playerKeys == GlobalVars.mapKeys: # Check the number of keys on the map versus the user's keys
                pygame.draw.rect(DISPLAYSURF, GlobalVars.green, (GlobalVars.goalXValue, GlobalVars.goalYValue, 20, 20)) # Draw an open or closed goal accordingly
            else:
                pygame.draw.rect(DISPLAYSURF, GlobalVars.red, (GlobalVars.goalXValue, GlobalVars.goalYValue, 20, 20))
            pygame.display.update() # Update the display
            return
        elif line[0] == 'm': # If the line begins with a m,
            GlobalVars.mapPackOver = True # Set map pack over to true,
            pygame.quit() # Exit pygame
            sys.exit() # Close the game
        lastPos = maps.tell() # Set the last position in the file
        counter += 1 # Increment the counter

if __name__ == '__main__':
    main()