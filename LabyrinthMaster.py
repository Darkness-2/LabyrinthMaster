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
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((400, 200))
    pygame.display.set_caption('Labyrinth Master')
    DISPLAYSURF.fill(GlobalVars.white)
    spamRect = pygame.Rect(10, 20, 200, 300)
    pygame.draw.rect(DISPLAYSURF, GlobalVars.blue, spamRect)
    mapOver = True
    while True:
        if mapOver == True:
            mapOver = False
            loadNewMap()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def loadNewMap()
    pass

if __name__ == '__main__':
    main()