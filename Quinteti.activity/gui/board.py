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

"""Board represents the game board, and its capable of paint its elements in a given surface."""

import pygame

from logic.game import GameState

from button import Button
from cell import Cell

file_dir = "gui/"

image_fondo = file_dir + "background.png"
image_tablero = file_dir + "tablero.png"
image_null = "nulo.bmp"
image_number = "<N>.png"
image_disabled_number = "<N>selected.png"
image_size = pygame.Rect(0, 0,  97,  97)

new_image_coords = (180,  87)
new_image = "quinteti-new.png"

instructions_coords = (950, 745)
instructions_button = "instructions_button.png"
instructions_image = "instructions.png"

player_win_image = "player_win.png"

font_name = "DejaVu Serif"  #"DejaVuLGCSerif.ttf"  # None  to load pygame default font
font_size = 24
user_font_color = (255, 255, 255)

"""Class Board keeps all the grafical elements as well as a reference to the logical game state."""
class Board:
    
    # Center of initial number positions
    number_locations = [
        ([756+138*0,  231+138*0]), 
        ([756+138*1,  231+138*0]), 
        ([756+138*2,  231+138*0]), 
        ([756+138*0,  231+138*1]), 
        ([756+138*1,  231+138*1]), 
        ([756+138*2,  231+138*1]), 
        ([756+138*0,  231+138*2]), 
        ([756+138*1,  231+138*2]), 
        ([756+138*2,  231+138*2])]
    
    screen = None
    # Center of board cells
    locations = [
        ([267, 228]),
        ([404, 228]),
        ([541, 228]),
        ([267, 367]),
        ([404, 367]),
        ([541, 367]),
        ([267, 510]),
        ([404, 510]),
        ([541, 510])]

    players_name_midleft_location = [
                             (200,  667), 
                             (200,  752)]
    
    players_score_center_location = [
                             (581,  667), 
                             (581,  752)]

    players_score_box_location = [
                             (173,  628), 
                             (173,  714)]

    def __init__(self, screen, game = None):
        self.font = None
        if font_name:
            self.font = pygame.font.SysFont(font_name, font_size)

        if not self.font:
            self.font = pygame.font.Font(None, font_size)
        
        self.screen = screen
        self.game = game
        self.showing_instructions = False
        self.init_board()

    def init_board (self):
        self.new_button = Button(new_image_coords, file_dir + new_image,  self.new_game)
        self.instructions_button = Button(instructions_coords, file_dir + instructions_button,  self._show_instructions)
        self.cells = []
        self.numbers = []
        self.lastSelectedBoardCell = None
        self.lastSelectedNumberCell = None
        
        self.backgroundImage = pygame.image.load(image_fondo)
        
        self._init_cells()
        self._init_numbers()
        
        # Creates a sprite group, with all the board visible elements inside
        self._paint_background()
        self.items = pygame.sprite.Group()
        self.items.add(self.new_button)
        self.items.add(self.instructions_button)
        for c in self.cells:
            if c.image:
                self.items.add( c )
            
        for n in self.numbers:
            if n.image:
                self.items.add( n )

    def new_game(self):
        self.game = GameState("", "")
        self.init_board()
        
    def _init_cells(self):
        i = 1
        for row in range(1,4):
            for col in range(1,4):
                if self.game:
                    number = self.game.get_cell(row, col)[0]
                else:
                    number = None
                location = self.locations[i-1]
                self.cells.append( Cell(location, self._get_number_name(number), i, image_size) )
                i += 1
    
    def _init_numbers(self):
        k = 0
        for location in self.number_locations:
            k += 1
            self.numbers.append(Cell(location, self._get_number_name(k), k, image_size)) 

    def set_players(self, name_player1, name_player2):
        self.game = GameState(name_player1, name_player2)
   
    def _paint_background(self):
        rect = self.backgroundImage.get_rect()
        rect.topleft = (0,  0)
        self.screen.blit(self.backgroundImage, rect)

    def _paint_winner(self,  i):
        image = pygame.image.load(file_dir + player_win_image)
        rect = image.get_rect()
        rect.topleft = self.players_score_box_location[i]
        self.screen.blit(image,  rect)
    
    def _paint_players_status(self):
        player1Name = "" 
        player2Name = ""
    
        if (self.game):
            for i in range(1,3):
                if self.game.get_enabled_player():
                    if self.game.get_enabled_player() == i:
                        self.font.set_bold(True)
                    else:
                        self.font.set_bold(False)
                else:
                    if self.game.get_player_score(i) >= self.game.get_player_score(3-i):
                        self._paint_winner(i-1)
                    
                player_name = self.game.get_player_name(i)
                #str_player = 'Jugador %s: %s' % (i, player_name)
                str_player = 'Jugador %s' % (i)
                name_surface = self.font.render(str_player, 1, user_font_color)
                name_rect = name_surface.get_rect()
                name_rect.midleft = self.players_name_midleft_location[i-1]
                self.screen.blit(name_surface, name_rect)
                
                player_score = self.game.get_player_score(i)
                str_player_score = '%s' % (player_score)
                score_surface = self.font.render(str_player_score, 1, user_font_color)
                score_rect = score_surface.get_rect()
                score_rect.center = self.players_score_center_location[i-1]
                self.screen.blit(score_surface, score_rect)

    def paintBoardElements(self):
        # Using an sprite group all the items are painted:
        
        #self.items.clear(self.screen,  self.backgroundImage)   # If only sprites are cleared, players scores remain
        self._paint_background()                                                  # Instead, the whole background is repainted
        self.items.draw(self.screen)
        self._paint_players_status()
        
        if self.showing_instructions:
            self._paint_instructions()

    def _paint_instructions(self):
        image = pygame.image.load(file_dir + instructions_image)
        rect = image.get_rect()
        rect.center = self.screen.get_rect().center
        self.screen.blit(image,  rect)

    def processXY(self, x, y):
        # If is showing instructions, it disables them
        if self.showing_instructions:
            self.showing_instructions = False
            return
        else:
            if self.instructions_button.coordsIn(x, y):
                self.instructions_button.callback()
        
        # Checks if the selected coordinate is a board cell
        isCell = False
        for c in self.cells:
            if c.coordsIn(x, y):
                isCell = True
                self.lastSelectedBoardCell = c
                if self.lastSelectedNumberCell != None:
                    row, col = c.get_pos()
                    player = self.game.get_enabled_player()
                    ok = self.game.make_move(row, col, self.lastSelectedNumberCell.idxCell, player)
                    if ok:
                        self.lastSelectedBoardCell.setImage( self._get_number_name(self.lastSelectedNumberCell.idxCell) )
                        self.items.add(self.lastSelectedBoardCell)
                        self.items.remove(self.lastSelectedNumberCell)
                        self.lastSelectedNumberCell.setImage(None)
                        self.lastSelectedNumberCell = None
                break
    
        # Checks if the selected coordinate is a number
        if isCell == False:
            for n in self.numbers:
                if n.coordsIn(x,y):
                    if self.lastSelectedNumberCell:
                        self.lastSelectedNumberCell.setImage( self._get_number_name(self.lastSelectedNumberCell.idxCell) )
                    self.lastSelectedNumberCell = n
                    n.setImage( self._get_disabled_number_name(n.idxCell) )
                    
        if self.new_button.coordsIn(x, y):
            self.new_button.callback()
        
        return True
    
    def _show_instructions(self):
        self.showing_instructions = True
    
    def _get_number_name(self, number):
        if (number == None) or (number == 0):
            return None
        else:
            return file_dir + image_number.replace("<N>", str(number))

    def _get_disabled_number_name(self, number):
        if (number == None) or (number == 0):
            return None
        else:
            return file_dir + image_disabled_number.replace("<N>", str(number))
