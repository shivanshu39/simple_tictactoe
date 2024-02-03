from tkinter import *


RED = '#d12f19'
GREEN = '#46cf27'
BG = '#b3bffc'
turns = 1

'''Check the win conditions
    this function access the text on buttons placed horizontally, vertically and diagonally to compare it to X and O. 
    if any of the condition equals X then player 1 is the winner, else if it equals to O then player 2 is the winner'''
def win_check():
    
    '''win conditions for player 1'''
    if A['text'] == B['text'] == C['text'] == 'X' or \
       D['text'] == E['text'] == F['text'] == 'X' or \
       G['text'] == H['text'] == I['text'] == 'X' or \
       A['text'] == D['text'] == G['text'] == 'X' or \
       B['text'] == E['text'] == H['text'] == 'X' or \
       C['text'] == F['text'] == I['text'] == 'X' or \
       A['text'] == E['text'] == I['text'] == 'X' or \
       G['text'] == E['text'] == C['text'] == 'X' :
        on_off_tile('disabled')
        game_end['text'] = 'Player 1 Wins!'
        game_end.place(relx=0.5, rely=0.5, width=350, height=70, anchor='center')
        return True
    
    '''win conditions for player 2'''
    if A['text'] == B['text'] == C['text'] == 'O' or \
       D['text'] == E['text'] == F['text'] == 'O' or \
       G['text'] == H['text'] == I['text'] == 'O' or \
       A['text'] == D['text'] == G['text'] == 'O' or \
       B['text'] == E['text'] == H['text'] == 'O' or \
       C['text'] == F['text'] == I['text'] == 'O' or \
       A['text'] == E['text'] == I['text'] == 'O' or \
       G['text'] == E['text'] == C['text'] == 'O' :
        on_off_tile('disabled')
        game_end['text'] = 'Player 2 Wins!'
        game_end.place(relx=0.5, rely=0.5, width=350, height=70, anchor='center')  # display win label for player 1
        return True
        
    global turns 
    turns += 1
    if turns > 9:
        on_off_tile('disabled') 
        game_end['text'] = "oh! It's a Tie"
        game_end['background'] = '#fce051'
        game_end.place(relx=0.5, rely=0.5, width=350, height=70, anchor='center')  # display win label for player 2
    return False
    

'''on click of tiles in game, update the player turn and display "X" or "O"
    based on the background color value of the labels, which player's turn it is, is decided'''
def update_tile(widget):
    
    
    if player_1['background'] == GREEN:
        widget['text'] = 'X'
        if win_check():
            return
        player_1['background'] = RED
        player_2['background'] = GREEN
        widget['state'] = 'disabled'
        
    elif player_2['background'] == GREEN:
        widget['text'] = 'O'
        if win_check():
            return
        player_2['background'] = RED
        player_1['background'] = GREEN
        widget['state'] = 'disabled'
        
      
'''reset the game'''
def reset_game():
    
    '''resetting background color values of all the labels'''
    player_1['background'] = GREEN
    player_2['background'] = RED
    game_end['background'] = GREEN
    
    '''resetting all the buttons to empty text and state to active'''
    A['text'] = ' '
    B['text'] = ' '
    C['text'] = ' '
    D['text'] = ' '
    E['text'] = ' '
    F['text'] = ' '
    G['text'] = ' '
    H['text'] = ' '
    I['text'] = ' '
    on_off_tile('active')
    
    '''resetting turns to 1 and forgetting win or tie label'''
    global turns
    turns = 1
    game_end.place_forget()
    
'''set tiles active or disabled'''
def on_off_tile(state: str):
    
    A['state'] = state
    B['state'] = state
    C['state'] = state
    D['state'] = state
    E['state'] = state
    F['state'] = state
    G['state'] = state
    H['state'] = state
    I['state'] = state

    
window = Tk()
screen_mid = str(int((window.winfo_screenwidth() / 2) - 200)) + '+' + str(int((window.winfo_screenheight() / 2) - 300))

window.geometry(f'400x600+{screen_mid}')
window.resizable(False, False)
window['bg'] = BG
window.title('TicTacToe Game')

play_board = Frame(window, bg=BG)
play_board.columnconfigure((0, 1, 2), weight=1, uniform='a')
play_board.rowconfigure((0, 1, 2), weight=1, uniform='a')

'''welcome label'''
Label(window, text="Let's Play", font=("arial", 30, "bold"), bg=BG).place(x=200, y=65, anchor='center')
Label(window, text="Tic Tac Toe", font=("arial", 16), bg=BG).place(x=200, y=110, anchor='center')

'''| A | B | C |'''
A = Button(play_board, text=' ', font=('arial', 20, 'bold'), disabledforeground=RED, command=lambda: update_tile(A))
A.grid(row=0, column=0, sticky='news', padx=2.5, pady=2.5)
B = Button(play_board, text=' ', font=('arial', 20, 'bold'), disabledforeground=RED, command=lambda: update_tile(B))
B.grid(row=0, column=1, sticky='news', padx=2.5, pady=2.5)
C = Button(play_board, text=' ', font=('arial', 20, 'bold'), disabledforeground=RED, command=lambda: update_tile(C))
C.grid(row=0, column=2, sticky='news', padx=2.5, pady=2.5)

'''| D | E | F |'''
D = Button(play_board, text=' ', font=('arial', 20, 'bold'), disabledforeground=RED, command=lambda: update_tile(D))
D.grid(row=1, column=0, sticky='news', padx=2.5, pady=2.5)
E = Button(play_board, text=' ', font=('arial', 20, 'bold'), disabledforeground=RED, command=lambda: update_tile(E))
E.grid(row=1, column=1, sticky='news', padx=2.5, pady=2.5)
F = Button(play_board, text=' ', font=('arial', 20, 'bold'), disabledforeground=RED, command=lambda: update_tile(F))
F.grid(row=1, column=2, sticky='news', padx=2.5, pady=2.5)

'''| G | H | I |'''
G = Button(play_board, text=' ', font=('arial', 20, 'bold'), disabledforeground=RED, command=lambda: update_tile(G))
G.grid(row=2, column=0, sticky='news', padx=2.5, pady=2.5)
H = Button(play_board, text=' ', font=('arial', 20, 'bold'), disabledforeground=RED, command=lambda: update_tile(H))
H.grid(row=2, column=1, sticky='news', padx=2.5, pady=2.5)
I = Button(play_board, text=' ', font=('arial', 20, 'bold'), disabledforeground=RED, command=lambda: update_tile(I))
I.grid(row=2, column=2, sticky='news', padx=2.5, pady=2.5)
play_board.place(relx=0.5, rely=0.45, height=250, width=250, anchor='center')

'''display player turn'''
player_turn = Frame(window, bg=BG)

player_1 = Label(player_turn, text='Player 1', background=GREEN, font=('arial', 16, 'bold'), anchor='center')
player_1.pack(side='left', expand=True, fill='both', padx=10, pady=5)

player_2 = Label(player_turn, text='Player 2', background=RED, font=('arial', 16, 'bold'), anchor='center')
player_2.pack(side='right', expand=True, fill='both', padx=10, pady=5)

player_turn.place(relx=0.5, rely=0.75, height=60, width=300, anchor='center')

'''Reset Game Button'''
reset_button = Button(window, text='Reset Game', command=reset_game, font=('arial', 12), anchor='center')
reset_button.place(relx=0.5, rely=0.87, anchor='center')

'''Winner or Tie label'''
game_end = Label(window, text='test', background=GREEN, font=('arial', 20, 'bold'), anchor='center')

window.mainloop()
