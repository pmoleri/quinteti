
class GameState:

    # Un constructor inicia la partida.
    def __init__(self, player_1, player_2, matrix_size=3, target_score=15):
        self.player_1_name=player_1
        self.player_2_name=player_2
        self.player_1_score=0
        self.player_2_score=0
        self.turn=1
        self.target_score=target_score
        self.matrix=[]
        self.state=[]
        for i in range(0, matrix_size):
            self.matrix.append([])
            self.state.append([])
            for j in range(0, matrix_size):
                self.matrix[i].append(0)
                self.state[i].append(None)
        self.numbers=range(1, len(self.matrix[0])*len(self.matrix)+1)
    
    # Un constructor que recupera el estado
    def fromString(string):
        dic = eval(string)
        state = dic['state']
        matrix = dic['matrix']
        size = len(matrix)
        game = GameState(dic['player_1_name'], dic['player_2_name'], size, dic['target_score'])
        game.matrix = matrix
        game.state = state
        game.player_1_name = dic['player_1_name']
        game.player_2_name = dic['player_2_name']
        game.player_1_score = dic['player_1_score']
        game.player_2_score = dic['player_2_score']
        
        #Saca los numeros jugados:
        for row in game.matrix:
            for number in row:
                if number in game.numbers:
                    game.numbers.remove(number)
        return game
    fromString = staticmethod(fromString)    # Crea un atributo estatico del tipo funcion
    
    # Persiste el estado actual del juego
    def serialization(self):
        return str(self)
    
    # Obtiene el estado de una casilla, tupla numero y jugador o None si esta vacia.
    #   get_cell(row : int, col : int): (number: int, player: int) or None
    def get_cell(self, row1, col1):
        row, col = (row1-1, col1-1)
        return (self.matrix[row][col], self.state[row][col])
    # Obtiene los numeros que se pueden jugar.
    #   get_available_numbers(): [int]
    def get_available_numbers(self): 
        return self.numbers
        
    # Realiza una jugada en una celda y retorna si se pudo realizar.
    #   make_move(row: int, col : int, number : int, player: int): bool
    def make_move(self, row1, col1, number, player):
        row, col = (row1-1, col1-1)
        if (self.state[row][col]==None):
            if (self.turn==player):
                if (number in self.numbers):
                    #obtengo una copia de la columna
                    col_list = [fila[col] for fila in self.matrix]
                    #obtengo una copia de la fila
                    row_list = self.matrix[row][:]
                        
                    score=0
                    score+=self.check_action(col_list, row, number)
                    score+=self.check_action(row_list, col, number)
                        
                    self.state[row][col]=self.turn
                    self.matrix[row][col]=number
                    self.numbers.remove(number)
                        
                    if self.turn == 1:
                        self.player_1_score += score
                        self.turn = 2
                    else:
                        self.player_2_score += score
                        self.turn = 1
                    return True
        return False
    
    # Rutina privada para verificar si la jugada suma puntos, se pasa una lista
    # que representa una columna o una fila y la jugada.
    def check_action(self, list, pos, number):
        list[pos] = number
        if 0 in list:
            return 0
        if sum(list) == self.target_score:
            return 1
        else:
            return 0
            
            
    # Jugador habilitado para jugar, o None si la partida termina.
    #   get_enabled_player(): int
    def get_enabled_player(self):
        if len(self.numbers) == 0:
            return None
        else:
            return self.turn
        
    # Puntaje de cada jugador
    #      get_player_score(player: int)
    def get_player_score(self, player):
        if player == 1 :
            return self.player_1_score
        else:
            return self.player_2_score
                
    # Obtiene el nombre de un jugador
    #   get_player_name(player: int): String
    def get_player_name(self, player):
        if player == 1 : 
            return self.player_1_name
        else:
            return self.player_2_name
                
    # Obtiene la cantidad de jugadores
    #   get_player_count(): int
    def get_player_count(self):
        return 2
    
    def __str__( self ):
        dic = {
               'state': self.state,
               'matrix': self.matrix,
               'player_1_name': self.player_1_name,
               'player_2_name': self.player_2_name,
               'player_1_score': self.player_1_score,
               'player_2_score': self.player_2_score,
               'target_score': self.target_score}
        return str(dic)
       

if __name__ == "__main__":
    var=GameState("Juan", "Pablo")
    print var.target_score
    
    var.make_move(0, 1, 2, 1)
    var.make_move(1, 1, 7, 2)
    var.make_move(2, 1, 6, 1)
    
    print var
    
    var2 = GameState.fromString( var.serialization() )
    print 'var2 %s' % (var2)
    print var2.get_player_name(1)
    
#    print var.matrix
#    print var.state
#    print var.player_1_score
#    print var.get_player_score(1)
#    print var.player_2_score
#    print var.get_player_score(2)
#    print var.get_player_name(1)
