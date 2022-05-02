import tkinter as tk
from Wordle_class import Wordle
from Wordle_data import main
                         
def onKeyPress(event):
    num_chars = sum([char.isalpha() for char in game.gameboard])
    print(event)
    # set the pressed key to the gameboard
    if(event.char.isalpha() and game.key_index<len(game.gameboard_finished)):
        game.gameboard[game.key_index] = event.char
        num_chars = sum([char.isalpha() for char in game.gameboard])
       
        if(num_chars<=len(game.gameboard_finished)):
            gui_gameboard = tk.Label(main_form ,font = "mincho 40 bold", fg = 'black', bg = 'white')
            gui_gameboard.grid(row=game.num_trials, column=game.key_index, padx=5 )
            gui_gameboard['text'] = str(game.gameboard[game.key_index])
            game.key_index +=1
              
    if(event.keysym == 'BackSpace' and game.key_index>0):
        game.key_index += -1
        game.gameboard[game.key_index]='_'
        
        gui_gameboard = tk.Label(main_form ,font = "mincho 40 bold", fg = 'black', bg = 'white')
        gui_gameboard.grid(row=game.num_trials, column=game.key_index, padx= 5 )
        gui_gameboard['text'] = str(game.gameboard[game.key_index])
        
        num_chars = sum([char.isalpha() for char in game.gameboard])
    
    if(num_chars == len(game.gameboard_finished)): 
       submit_but.config(state="active")
       if(event.keysym=='Return'):
           submit_click()
    else:
        submit_but.config(state="disable")
    
def submit_click():
    game.is_in_dictionary(game.gameboard)
    
    if(game.is_dict):
        game.define_colors(game.gameboard)
        game.set_colors(main_form)
        populate_board(game.keyboard_en)
        game.get_status()
        submit_but.grid(row=game.num_trials, column=7)
    
def populate_board(keyboard):                                                       # Generates Form with keyboard buttons 

    startpos = 440
    xpos_ini = 20
    xpos = xpos_ini
    ypos = startpos
    
    for c in range(len(keyboard)):
        # Formating Buttons
        if(c == 10):
            ypos = startpos + 25
            xpos = xpos_ini+10
        elif(c == 19):
            ypos = startpos + 50
            xpos = xpos_ini+20
        # print the button
        letter = tk.Label(main_form, text = keyboard[c].upper(),font = "mancho 20", bg = game.colors_keyboard[c])
        letter.place(bordermode=tk.OUTSIDE, height=25, width=25,x=xpos,y=ypos)
        xpos = xpos + 25
        
def key_press():
    main_form.bind('<KeyPress>', onKeyPress)  

def create_submit_button():
    submit_but = tk.Button(main_form,text = 'submit',state = 'disable',bg = 'white', command = lambda: submit_click())
    submit_but.grid(row=game.num_trials, column=7,padx=30, ipady=10)
    return submit_but
 
def create_legend():
    tk.Label(main_form, text="LEGEND",font = "mincho 15", bg = 'white').place(x=0,y=320)
    tk.Label(main_form, text="Character in correct position",font = "mincho 10",bg='green').place(x=0,y=340)
    tk.Label(main_form, text="Character in wrong position but in word",font = "mincho 10", bg='yellow').place(x=0,y=360)
    tk.Label(main_form, text="Character not in word",font = "mincho 10", bg = 'gray').place(x=0,y=380)



###########################
# Window
en,en_long = main()
main_form = tk.Tk()                                                          
main_form.title("Wordle")
main_form.geometry("300x550")
main_form.resizable(True, False)
main_form.configure(background='white')
    

game = Wordle(en)
game.set_matrix(main_form)

key_press()
submit_but = create_submit_button()
create_legend()
populate_board(game.keyboard_en)

main_form.mainloop()
