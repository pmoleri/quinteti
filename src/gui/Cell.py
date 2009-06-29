import pygame

class Cell(pygame.sprite.Sprite):
    def __init__(self, initial_position, nomImage, idxCell,  size):

        pygame.sprite.Sprite.__init__(self)
        
        self.idxCell = idxCell
        
        self.rect = size.move(0, 0)             # Attemping to move creates a copy
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

# Codigo para debug de este modulo:
if __name__ == "__main__":
    cell = Cell([0, 0], "nulo.bmp", 6)
    row, col = cell.get_pos()
    print "%s %s" % (row, col)
