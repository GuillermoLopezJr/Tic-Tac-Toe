#Author - Guillermo Lopez Jr.
## add a menu bar to restart
## add tkinter.messagebox to display who wins and display play again or quite options
#fix resize

import tkinter
from tkinter import Frame

class TicTacToe:

    def __init__(self):

        self.initWindow()
        self.drawBoard()
        self.drawBottomFrame()

        self.startGame()
        
        tkinter.mainloop()
        
    def initWindow(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("534x647")
        self.main_window.title("Tic Tac Toe")
        self.main_window.configure(bg = "white")
        self.main_window.maxsize(534,647)
        self.bottom_Frame = tkinter.Frame(self.main_window, height = 100, width = 546, bg = "black")
        self.bottom_Frame.place(x = 0, y = 547)

    def startGame(self):
        self.player1 = "X" 
        self.player2 = "O"
        
        self.current_player = self.player1
        self.turns = 0
        self.game_over = False
        
    def playAgain(self):
        """ restarts some variables and
             clears the board to play again"""

        self.startGame()
        self.drawBoard()
        
    def initScores(self):
        
        #stringvar to update score labels
        self.player1_score = tkinter.StringVar()
        self.player2_score = tkinter.StringVar()
        self.tie_score = tkinter.StringVar()

        #int variable to put in string variables

        self.p1_score = self.p2_score = self.t_score = 0

        #sets the init score
        self.player1_score.set(self.p1_score)
        self.player2_score.set(self.p2_score)
        self.tie_score.set(self.t_score)
        
        
    def drawBottomFrame(self):
        """ initilizes the scores and places them
              on the bottom of the screen"""

        self.initScores()
        
        self.label_Font = ("Arial", 24, "bold")

        #init player label
        self.player1_label = tkinter.Label(self.bottom_Frame, text = "Player 1: (X)", bg = "black",fg = "white" , font = self.label_Font)
        self.player2_label = tkinter.Label(self.bottom_Frame, text = "Player 2: (O)", bg = "black", fg = "white", font = self.label_Font)
        self.tie_label = tkinter.Label(self.bottom_Frame, text = "TIES: ", bg = "black", fg = "white", font = self.label_Font)

        #place player label
        self.player1_label.place(x = 0, y = 10)
        self.player2_label.place(x = 340, y = 10)
        self.tie_label.place(x = 215, y = 10)

        #init score labels
        self.label1_score_label = tkinter.Label(self.bottom_Frame, textvariable = self.player1_score, bg = "black", fg = "white", font = ("Arial", 30, "bold"))
        self.label2_score_label = tkinter.Label(self.bottom_Frame, textvariable = self.player2_score, bg = "black", fg = "white", font = ("Arial", 30, "bold"))
        self.tie_score_label = tkinter.Label(self.bottom_Frame, textvariable = self.tie_score, bg = "black", fg = "white", font = ("Arial", 30, "bold"))

        #place score labels
        self.label1_score_label.place(x = 50, y = 50)
        self.label2_score_label.place(x = 400, y = 50)
        self.tie_score_label.place(x = 240, y = 50)
        
    def drawBoard(self):
        """ initilizes the board and draws it using buttons"""
        
        self.button_Font = ("Arial", 68, "bold")
        self.button_List = []
        
        for boxes in range(9):
            self.button_List.append(tkinter.Button(self.main_window, text = "",
                                    font = self.button_Font, bg = "black", fg = "white", width = 3, height = 1,
                                     command = lambda pos = boxes: self.boxPressed(pos)))
        index = 0
        for r in range(3):
            for col in range(3):
                self.button_List[index].grid(row = r, column = col)
                index += 1
                
    def boxPressed(self, position):
        """handles the mouse clicks"""

        if(self.game_over == True):
            self.playAgain()

        self.button_List[position].config(text = self.current_player)
        self.turns += 1
        
        #can't overide existing move
        self.button_List[position].config(state = "disabled", disabledforeground = "white")
        
        #check for winner or cat game
        isWinner = self.checkWinner(self.current_player)
        isCat = self.isCatGame(self.turns)
        
        if(isWinner):
            if(self.current_player == self.player1):
                self.p1_score += 1
                self.player1_score.set(self.p1_score)
            elif(self.current_player == self.player2):
                self.p2_score += 1
                self.player2_score.set(self.p2_score)
        elif(isCat):
            self.t_score += 1
            self.tie_score.set(self.t_score);    
        else:
            self.current_player = self.player1 if self.current_player == self.player2 else self.player2

        if(isWinner or isCat):
            self.game_over = True
            self.enableButtons()

            
    def enableButtons(self):
        for index in range(9):
                self.button_List[index].config(state = "normal")

    def isCatGame(self, turns):
        return (turns == 9)

    def checkWinner(self, player):
        """returns true if there is a winner"""
        
        ##-------------------------------------##
        ##          horizontal wins            ##
        ##-------------------------------------##
        if(self.button_List[0]["text"] == player and self.button_List[1]["text"] == player and self.button_List[2]["text"] == player):
            for index in range(0,3):
                self.button_List[index].config(disabledforeground = "red", fg = "red")
            return True
            
        elif(self.button_List[3]["text"] == player and self.button_List[4]["text"] == player and self.button_List[5]["text"] == player):
            for index in range(3, 6):
                self.button_List[index].config(disabledforeground = "red", fg = "red")
            return True
            
        elif(self.button_List[6]["text"] == player and self.button_List[7]["text"] == player and self.button_List[8]["text"] == player):
            for index in range(6,9):
                self.button_List[index].config(disabledforeground = "red", fg = "red")
            return True
        ##--------------------------------------##
        ##            Vertical wins             ##
        ##--------------------------------------##
        elif(self.button_List[0]["text"] == player and self.button_List[3]["text"] == player and self.button_List[6]["text"] == player):
            for index in range(0,7,3):
                self.button_List[index].config(disabledforeground = "red", fg = "red")
            return True 
        elif(self.button_List[1]["text"] == player and self.button_List[4]["text"] == player and self.button_List[7]["text"] == player):
            for index in range(1,8,3):
                self.button_List[index].config(disabledforeground = "red", fg = "red")
            return True
        elif(self.button_List[2]["text"] == player and self.button_List[5]["text"] == player and self.button_List[8]["text"] == player):
            for index in range(2,9,3):
                self.button_List[index].config(disabledforeground = "red", fg = "red")
            return True
        ##--------------------------------------##
        ##          Diagonal wins               ##
        ##--------------------------------------##
        elif(self.button_List[0]["text"] == player and self.button_List[4]["text"] == player and self.button_List[8]["text"] == player):
            for index in range(0,9,4):
                self.button_List[index].config(disabledforeground = "red", fg = "red")
            return True
        elif(self.button_List[2]["text"] == player and self.button_List[4]["text"] == player and self.button_List[6]["text"] == player):
            for index in range(2,7,2):
                self.button_List[index].config(disabledforeground = "red", fg = "red")
            return True
        else:
            return False
        
App = TicTacToe()
