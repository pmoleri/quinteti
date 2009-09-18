import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, initial_position, nomImage,  callback):

        pygame.sprite.Sprite.__init__(self)
        
        self.setImage(nomImage)
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position     # Moves the recteangle to its predetermined center
        
        self.callback = callback
    
    def coordsIn(self, x, y):
        #print "Test x: %s < %s < %s Test y: %s < %s < %s" % (self.rect.left,  x,  self.rect.right,  self.rect.top,  y,  self.rect.bottom)
        if ( self.rect.collidepoint(x, y) ):
            return True
        return False
    
    def setImage(self, nomImage):
        if nomImage:
            self.image = pygame.image.load(nomImage)
        else:
            self.image = None

# Codigo para debug de este modulo:
#if __name__ == "__main__":

