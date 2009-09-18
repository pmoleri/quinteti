#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#
# Copyright 2008, 2009 Pablo Moleri, ceibalJAM
# This file is part of Quinteti.
#
# Quinteti is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Quinteti is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Quinteti.  If not, see <http://www.gnu.org/licenses/>.

import pygame

"""Cell is a PyGame Sprite, capable of loading an image and retain a cell identifier."""

class Cell(pygame.sprite.Sprite):
    def __init__(self, initial_position, nomImage, idxCell,  size_rect):

        pygame.sprite.Sprite.__init__(self)
        
        self.idxCell = idxCell
        
        self.rect = size_rect.move(0, 0)             # Attempting to move creates a copy
        self.rect.center = initial_position     # Moves the recteangle to its predetermined center
        
        self.setImage(nomImage)
    
    def coordsIn(self, x, y):
        #print "Test x: %s < %s < %s Test y: %s < %s < %s" % (self.rect.left,  x,  self.rect.right,  self.rect.top,  y,  self.rect.bottom)
        if ( self.rect.collidepoint(x, y) ):
            return True
        return False
    
    def setImage(self, nomImage):
        if nomImage:
            self.image = pygame.image.load(nomImage)
            self.nameImage = nomImage
        else:
            self.image = None
            self.nameImage = None
        
    def get_pos(self):
        row = (self.idxCell - 1) / 3 + 1
        col = (self.idxCell - 1) % 3 + 1
        return row, col

if __name__ == "__main__":
    '''Debug Code.'''
    image_size = pygame.Rect(0, 0,  97,  97)
    cell = Cell([0, 0], "1.png", 6, image_size)
    row, col = cell.get_pos()
    print "%s %s" % (row, col)
