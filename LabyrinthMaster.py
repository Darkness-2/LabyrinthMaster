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

import jLibrary
import GlobalVars
import pygame
from pygame.locals import *
import sys

def main():
    maps = open('mainMaps.txt')
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((400, 200))
    pygame.display.set_caption('Labyrinth Master')
    DISPLAYSURF.fill(GlobalVars.white)
    while True:
        if GlobalVars.mapOver == True:
            GlobalVars.mapOver = False
            loadNewMap(maps, DISPLAYSURF)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    playerMovement('up', DISPLAYSURF)
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
        pygame.display.update()

def playerMovement(direction, DISPLAYSURF):
    goalFound = False
    wallFound = False
    while goalFound == False and wallFound == False:
        originalXValue = GlobalVars.playerXValue
        originalYvalue = GlobalVars.playerYValue
        if direction == 'up':
            oneUp = [GlobalVars.playerXValue, GlobalVars.playerYValue - 1]
            found = False
            counter = 0
            while found == False:
                if GlobalVars.mapArray[counter][:2] == oneUp:
                    found = True
                    nextBlock = GlobalVars.mapArray[counter]
                counter += 1
        elif direction == 'down':
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
        if nextBlock[2] == 'w':
            wallFound = True
        elif nextBlock[2] == 'g':
            GlobalVars.playerXValue = nextBlock[0]
            GlobalVars.playerYValue = nextBlock[1]
            if GlobalVars.playerKeys == GlobalVars.mapKeys:
                goalFound = True
                GlobalVars.mapOver = True
                pygame.draw.rect(DISPLAYSURF, GlobalVars.yellow, (GlobalVars.playerXValue * 20, GlobalVars.playerYValue * 20, 20, 20))
                pygame.draw.rect(DISPLAYSURF, GlobalVars.gray, (originalXValue * 20, originalYvalue * 20, 20, 20))
                pygame.display.update()
                pygame.time.delay(500)
            else:
                pygame.draw.rect(DISPLAYSURF, GlobalVars.red, (GlobalVars.playerXValue * 20, GlobalVars.playerYValue * 20, 20, 20))
                pygame.draw.rect(DISPLAYSURF, GlobalVars.gray, (originalXValue * 20, originalYvalue * 20, 20, 20))
                pygame.display.update()
                pygame.time.delay(30)
        elif nextBlock[2] == ' ':
            GlobalVars.playerXValue = nextBlock[0]
            GlobalVars.playerYValue = nextBlock[1]
            pygame.draw.rect(DISPLAYSURF, GlobalVars.blue, (GlobalVars.playerXValue * 20, GlobalVars.playerYValue * 20, 20, 20))
            pygame.draw.rect(DISPLAYSURF, GlobalVars.gray, (originalXValue * 20, originalYvalue * 20, 20, 20))
            pygame.display.update()
            pygame.time.delay(30)
        elif nextBlock[2] == 'k':
            GlobalVars.playerXValue = nextBlock[0]
            GlobalVars.playerYValue = nextBlock[1]
            GlobalVars.mapArray[counter - 1] = [nextBlock[0], nextBlock[1], ' ']
            GlobalVars.playerKeys += 1
            if GlobalVars.playerKeys == GlobalVars.mapKeys:
                pygame.draw.rect(DISPLAYSURF, GlobalVars.green, (GlobalVars.goalXValue, GlobalVars.goalYValue, 20, 20))
            pygame.draw.rect(DISPLAYSURF, GlobalVars.blue, (GlobalVars.playerXValue * 20, GlobalVars.playerYValue * 20, 20, 20))
            pygame.draw.rect(DISPLAYSURF, GlobalVars.gray, (originalXValue * 20, originalYvalue * 20, 20, 20))
            pygame.display.update()
            pygame.time.delay(30)

def loadNewMap(maps, DISPLAYSURF):
    del GlobalVars.mapArray[:]
    xValue = 0
    yValue = 0
    for line in maps:
        line = line.strip()
        xValue = 0
        if line[0] == 't':
            GlobalVars.mapTitle = line[1:]
            pygame.display.set_caption(GlobalVars.mapTitle)
        elif line[0] == 'l':
            line = line[1:]
            for letter in line:
                if letter == 'w':
                    pygame.draw.rect(DISPLAYSURF, GlobalVars.black, (xValue, yValue, 20, 20))
                    GlobalVars.mapArray.append([xValue / 20, yValue / 20, 'w'])
                    xValue += 20
                elif letter == ' ':
                    pygame.draw.rect(DISPLAYSURF, GlobalVars.gray, (xValue, yValue, 20, 20))
                    GlobalVars.mapArray.append([xValue / 20, yValue / 20, ' '])
                    xValue += 20
                elif letter == 's':
                    pygame.draw.rect(DISPLAYSURF, GlobalVars.blue, (xValue, yValue, 20, 20))
                    GlobalVars.playerXValue = xValue / 20
                    GlobalVars.playerYValue = yValue / 20
                    GlobalVars.mapArray.append([xValue / 20, yValue / 20, ' '])
                    xValue += 20
                elif letter == 'g':
                    GlobalVars.goalXValue = xValue
                    GlobalVars.goalYValue = yValue
                    GlobalVars.mapArray.append([xValue / 20, yValue / 20, 'g'])
                    xValue += 20
                elif letter == 'k':
                    pygame.draw.rect(DISPLAYSURF, GlobalVars.yellow, (xValue, yValue, 20, 20))
                    GlobalVars.mapArray.append([xValue / 20, yValue / 20, 'k'])
                    GlobalVars.mapKeys += 1
                    xValue += 20
            yValue += 20
        elif line[0] == 'e':
            if GlobalVars.playerKeys == GlobalVars.mapKeys:
                pygame.draw.rect(DISPLAYSURF, GlobalVars.green, (GlobalVars.goalXValue, GlobalVars.goalYValue, 20, 20))
            else:
                pygame.draw.rect(DISPLAYSURF, GlobalVars.red, (GlobalVars.goalXValue, GlobalVars.goalYValue, 20, 20))
            return
            pygame.display.update()

if __name__ == '__main__':
    main()