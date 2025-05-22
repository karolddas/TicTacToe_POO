#TicTacToe_Game

print("Welcome to the Tic Tac Toe Game!\nThe player number one will be playing with the X symbol, and the player number two with the O symbol.\nRemember that to win you'll have to make a line of three of your symbols in any direction.\nGood luck to both!")

TicTacToe= [ 1, 2, 3, 
             4, 5, 6,
             7, 8, 9,]
win_combos=[[1, 2, 3],  # fila 1
            [4, 5, 6],  # fila 2
            [7, 8, 9],  # fila 3
            [1, 4, 7],  # columna 1
            [2, 5, 8],  # columna 2
            [3, 6, 9],  # columna 3
            [1, 5, 9],  # diagonal \
            [3, 5, 7]]  # diagonal /
used_numbers=[]
times=0
game_over=False

def PrintTTT():
    for i in range (0,9,3):
        print(TicTacToe[i], TicTacToe[i+1], TicTacToe[i+2])

def Player_1_X():
    number_x=int(input("Player 1 choose the number you want to play with your symbol X "))
    while number_x>9 or number_x<1 or number_x in used_numbers:
        number_x=int(input("ERROR : That number is already played or maybe you inserted and invalid number try again with another number between 1 and 9."))
    if number_x not in used_numbers:
        used_numbers.append(number_x)
        TicTacToe[number_x - 1] = 'X'
      
def Player_2_O():
    number_O=int(input("Player 2 choose the number you want to play with your symbol O "))
    while number_O>9 or number_O<1 or number_O in used_numbers:
        number_O=int(input("ERROR : That number is already played or maybe you inserted and invalid number try again with another number between 1 and 9."))
    if number_O not in used_numbers:
        used_numbers.append(number_O)
        TicTacToe[number_O - 1] = 'O'
    
def Analyze(symbol):
    for combo in win_combos:
        if TicTacToe[combo[0]-1] == TicTacToe[combo[1]-1] == TicTacToe[combo[2]-1] == symbol:
            for i in range (0,9,3):
                 print(TicTacToe[i], TicTacToe[i+1], TicTacToe[i+2])
            print (f"We have a winner! {symbol} wins")
            return True
    return False

PrintTTT()

while times<9 and game_over==False:
    Player_1_X()
    game_over=Analyze("X")
    PrintTTT()
    times+=1
    if game_over==True or times == 9:
        break
    Player_2_O()
    game_over=Analyze("O")
    PrintTTT()
    times+=1
    if game_over==True or times == 9:
        break
if times>=9 and game_over==False:
        print("It´s a match! Nobody wins")

    


    


