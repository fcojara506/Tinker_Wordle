import random
import tkinter as tk                                                  
from tkinter import messagebox                                            

class Wordle:
    def __init__(self,word_list):
        self.word_list = word_list                                                      
        self.num_lives = 5
        self.num_trials = 0
        self.key_index = 0
        self.is_dict = False
        self.colors = list
        self.keyboard_en = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        self.colors_keyboard = ['white' for char in self.keyboard_en]
        self.end_state = False
        self.played_word = random.choice(self.word_list)
        self.gameboard = ['_'] * len(self.played_word)
        self.gameboard_finished = list(self.played_word)
    
    def restart_program(self):
        self.__init__(self.word_list)
        self.set_Word()                                                        
        self.create_board()                              
        self.set_finished_board()
        self.set_matrix()
        
    def set_matrix(self,main_form):
        w = 0
        for i in range(self.num_lives):
            for j in range(len(self.played_word)):
                gui_gameboard = tk.Label(main_form ,font = "mincho 40 bold", bg = 'white')
                gui_gameboard.grid(row=i, column=j,padx=5)
                if(w< len(self.played_word)*self.num_lives):
                    gui_gameboard['text'] = str(self.gameboard[j])
                    w += 1        
                    
    def get_status(self):
        self.num_trials += 1
        self.key_index = 0
        if(self.gameboard == self.gameboard_finished):
            self.end_state = True
            messagebox.showinfo("Congratulation", "You won")
            self.restart_program()
        elif(self.num_trials == self.num_lives):
            messagebox.showinfo("Try again", "The answer was: " + self.played_word.upper())
            self.restart_program()
        self.gameboard = ['_'] * len(self.played_word)
    
    def set_colors(self,main_form):
        for i in range(self.key_index):
            gui_gameboard = tk.Label(main_form ,font = "mincho 40 bold", bg = self.colors[i])
            gui_gameboard.grid(row=self.num_trials, column=i, padx=5)
            gui_gameboard['text'] = str(self.gameboard[i])
    
    def is_in_dictionary(self,word):
        word=''.join(word)
        
        if(word in self.word_list):
            self.is_dict = True
        else:
            self.is_dict = False
            messagebox.showinfo("Error", "this word is not in the dictionary")
            
    def define_colors(self,word):
       # print(self.played_word)
        if(len(word) == len(self.played_word)):
            colors_list = []
            for position,char in enumerate(word):
               indexes = [i for i, x in enumerate(self.played_word) if char == x]
               index_keyboard = self.keyboard_en.index(char)
               
               print(index_keyboard)
               
               if(len(indexes)>0):                  
                   if(position in indexes):
                       colors_list.append('green')
                       self.colors_keyboard[index_keyboard]='green'
                   else:
                       colors_list.append('yellow')
                       self.colors_keyboard[index_keyboard]='yellow'
               else:
                   colors_list.append('gray')
                   self.colors_keyboard[index_keyboard]='gray'
        self.colors = colors_list          

