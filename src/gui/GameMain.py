import pygame, olpcgames, logging
from olpcgames import pausescreen
from pygame.locals import *

from BoardUI import BoardUI

from logic.GameState import GameState

#import logic.Mesh

import os

log = logging.getLogger( 'quinteti run' )
log.setLevel( logging.DEBUG )

MAX_FPS = 25                # Max frames per second
SLEEP_TIMEOUT = 25     # Seconds until the PauseScreen if no events show up

# El modulo se llama desde run.py.
def main():
    pygame.init()
    
    internal_size = (1200,  825)        # The game is designed to work in this size (xo display size)
    target_size = (900, 619)             # The game will be sown in this size, useful for testing in regular PCs with less resolution than xo
    
    flags = 0
    if olpcgames.ACTIVITY:
        # Running as Activity
        target_size = olpcgames.ACTIVITY.game_size
        #logic.Mesh.init_mesh(log)                                  # Mesh isn't ready in this version
    #else:
        # Uncomment this if want to execute fullscreen on regular PCs
        # flags = pygame.FULLSCREEN
    real_screen = pygame.display.set_mode(target_size,  flags)
    
    # The scale factor beetween internal and target
    if internal_size == target_size:
        scale = None
        internal_screen = real_screen   # The game works directly on the real screen
    else:
        # Running on regular PC, the screen its scaled to te target_size
        internal_screen = pygame.Surface(internal_size)
        scale = (internal_size[0] / float(target_size[0]),  internal_size[1] / float(target_size[1]) )
    
    # Creates a new logic game, player names aren't used without mesh
    game = GameState("Jugador1", "Jugador2") 
    boardUI = BoardUI(internal_screen, game)
    boardUI.paintBoardElements()
    
    pygame.display.update()
    
    clock = pygame.time.Clock()
    
    # Comienza el bucle principal
    update = True       # La primera vez tiene que pintar la pantalla
    running = True
    while running:
        
        # Waits for events, if none the game pauses:
        # http://wiki.laptop.org/go/Game_development_HOWTO#Reducing_CPU_Load
        milliseconds = clock.tick(MAX_FPS)                              # waits if the game is running faster than MAX_FPS
        events = pausescreen.get_events(SLEEP_TIMEOUT)     # Event-management loop with support for pausing after X seconds (20 here)
        
        if events:
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE):
                    running = False
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if scale:
                        [x, y] = [coord*s for (coord, s) in zip(event.pos, scale)]       # Multiplica las coordenadas realeas por el factor
                                                                                                                    # para llevarlas a coordenadas internas
                    else:
                        (x, y) = event.pos

                    boardUI.processXY(x, y)
                    update = True
                
                if event.type == pygame.USEREVENT:
                    if event.code == olpcgames.FILE_READ_REQUEST:
                        game = read_file(event.filename)
                        log.debug("Loaded:" + game.serialization())
                        boardUI = BoardUI(internal_screen, game)
                        update = True
                    if event.code == olpcgames.FILE_WRITE_REQUEST:
                        save_file(event.filename, game)
            
            if update == True:
                boardUI.paintBoardElements()
                if scale:
                    pygame.transform.scale(internal_screen, target_size, real_screen)
                update = False
            
            pygame.display.update()
        
    # Una vez que sale del loop manda la senal de quit para que cierre la ventana
    pygame.quit()

def save_file(file, game):
    string = game.serialization()
    fsock = open(file, 'w')
    fsock.write(string)
    fsock.close()

def read_file(file):
    fsock = open(file, "r")
    string = fsock.read()
    fsock.close()
    return GameState.fromString(string)

# Codigo para debug de este modulo:
if __name__ == "__main__":
    logging.basicConfig()
    main()
