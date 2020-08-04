# Hangman Game, You may contribute by Adding different words in the WordList File, You Have My Thanks

import random
from tkinter import *
from tkinter import messagebox
from WordList import Words
# Required 5 Variables for the main game logic
global game, dashes, tries, guessed, word


# Defining main game logic in a function so that we can recall it when the game is over
def main_game():
    global game, dashes, tries, guessed, word
    game = Tk()
    game.title('HangMan')
    game.geometry('1308x736')

    # Variable "a" for positioning the buttons in GUI
    a = 100

    word = random.choice(Words).upper()  # Making all letters Uppercase to save case sensitive errors

    dashes = "-" * len(word)  # Converting random word into dashes
    printDashes = Label(game, text=dashes, font=("Arial", 30))
    printDashes.place(x=200, y=200)

    tries = 6
    printTries = Label(game, text=f"You have {tries} tries left", font=("Arial", 20))
    printTries.place(x=850, y=600)

    guessed = False

    def refresh():  # A function to restart the game after it is over
        game.destroy()
        main_game()

    def show_hang():  # A function to display hangman using Text only
        global tries
        hangman = [
            """
                       --------
                       |      |
                        |     O
                        |     \\|/
                       |      |
                        |     / \\
                       -
                    """,
            # Sixth Try
            """
                       --------
                       |      |
                        |     O
                        |     \\|/
                       |      |
                       |      / 
                       -
                    """,
            # Fifth Try
            """
                       --------
                       |      |
                        |     O
                        |     \\|/
                       |      |
                      |      
                       -
                    """,
            # Fourth Try
            """
                       --------
                       |      |
                        |     O
                       |     \\|
                       |      |
                     |     
                       -
                    """,
            # Third Try
            """
                       --------
                       |      |
                        |     O
                       |      |
                       |      |
                     |     
                       -
                    """,
            # Second Try
            """
                       --------
                       |      |
                        |     O
                    |    
                      |      
                     |     
                       -
                    """,
            # First Try
            """
                       --------
                       |      |
                      |      
                    |    
                      |      
                     |     
                       -
                    """
        ]
        for number in hangman:
            hang = Label(game, text=hangman[tries], font=("Arial", 30))
            hang.place(x=700, y=100)  # # #

    show_hang()

    def check_game_lost():  # Checking after each user input if the game has ended or not
        global dashes, tries, guessed, word
        if tries == 0:
            printDashes.configure(text=f"The Word was {word}", font=("Arial", 30))
            if messagebox.askyesno("You Lost", "Do You Want To Try Again?"):
                refresh()
            else:
                game.destroy()

        elif "-" not in dashes:
            printTries.configure(text="Congrats!! You Guessed the Word", font=("Arial", 20))
            printTries.place(x=750, y=600)
            if messagebox.askyesno("You Won", "Do You Want To Try Again?"):
                refresh()
            else:
                game.destroy()

# Functions for all alpha inputs with the game logic
    def a_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "A" not in word:
                btn_a.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "A" in word:
                indices = [i for i, letter in enumerate(word) if letter == "A"]
                for index in indices:
                    word_as_list[index] = "A"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_a.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def b_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "B" not in word:
                btn_b.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "B" in word:
                indices = [i for i, letter in enumerate(word) if letter == "B"]
                for index in indices:
                    word_as_list[index] = "B"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_b.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def c_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "C" not in word:
                btn_c.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "C" in word:
                indices = [i for i, letter in enumerate(word) if letter == "C"]
                for index in indices:
                    word_as_list[index] = "C"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_c.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def d_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "D" not in word:
                btn_d.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "D" in word:
                indices = [i for i, letter in enumerate(word) if letter == "D"]
                for index in indices:
                    word_as_list[index] = "D"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_d.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def e_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "E" not in word:
                btn_e.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "E" in word:
                indices = [i for i, letter in enumerate(word) if letter == "E"]
                for index in indices:
                    word_as_list[index] = "E"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_e.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def f_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "F" not in word:
                btn_f.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "F" in word:
                indices = [i for i, letter in enumerate(word) if letter == "F"]
                for index in indices:
                    word_as_list[index] = "F"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_f.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def g_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "G" not in word:
                btn_g.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "G" in word:
                indices = [i for i, letter in enumerate(word) if letter == "G"]
                for index in indices:
                    word_as_list[index] = "G"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_g.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def h_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "H" not in word:
                btn_h.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "H" in word:
                indices = [i for i, letter in enumerate(word) if letter == "H"]
                for index in indices:
                    word_as_list[index] = "H"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_h.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def i_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "I" not in word:
                btn_i.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "I" in word:
                indices = [i for i, letter in enumerate(word) if letter == "I"]
                for index in indices:
                    word_as_list[index] = "I"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_i.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def j_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "J" not in word:
                btn_j.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "A" in word:
                indices = [i for i, letter in enumerate(word) if letter == "J"]
                for index in indices:
                    word_as_list[index] = "J"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_j.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def k_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "K" not in word:
                btn_k.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "K" in word:
                indices = [i for i, letter in enumerate(word) if letter == "K"]
                for index in indices:
                    word_as_list[index] = "K"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_k.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def l_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "L" not in word:
                btn_l.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                break
            elif "L" in word:
                indices = [i for i, letter in enumerate(word) if letter == "L"]
                for index in indices:
                    word_as_list[index] = "L"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_l.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def m_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "M" not in word:
                btn_m.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "M" in word:
                indices = [i for i, letter in enumerate(word) if letter == "M"]
                for index in indices:
                    word_as_list[index] = "M"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_m.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def n_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "N" not in word:
                btn_n.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "N" in word:
                indices = [i for i, letter in enumerate(word) if letter == "N"]
                for index in indices:
                    word_as_list[index] = "N"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_n.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def o_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "O" not in word:
                btn_o.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "O" in word:
                indices = [i for i, letter in enumerate(word) if letter == "O"]
                for index in indices:
                    word_as_list[index] = "O"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_o.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def p_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "P" not in word:
                btn_p.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "P" in word:
                indices = [i for i, letter in enumerate(word) if letter == "P"]
                for index in indices:
                    word_as_list[index] = "P"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_p.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def q_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "Q" not in word:
                btn_q.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "Q" in word:
                indices = [i for i, letter in enumerate(word) if letter == "Q"]
                for index in indices:
                    word_as_list[index] = "Q"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_q.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def r_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "R" not in word:
                btn_r.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "R" in word:
                indices = [i for i, letter in enumerate(word) if letter == "R"]
                for index in indices:
                    word_as_list[index] = "R"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_r.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def s_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "S" not in word:
                btn_s.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "S" in word:
                indices = [i for i, letter in enumerate(word) if letter == "S"]
                for index in indices:
                    word_as_list[index] = "S"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_s.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def t_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "T" not in word:
                btn_t.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "T" in word:
                indices = [i for i, letter in enumerate(word) if letter == "T"]
                for index in indices:
                    word_as_list[index] = "T"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_t.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def u_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "U" not in word:
                btn_u.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "U" in word:
                indices = [i for i, letter in enumerate(word) if letter == "U"]
                for index in indices:
                    word_as_list[index] = "U"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_u.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def v_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "V" not in word:
                btn_v.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "V" in word:
                indices = [i for i, letter in enumerate(word) if letter == "V"]
                for index in indices:
                    word_as_list[index] = "V"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_v.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def w_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "W" not in word:
                btn_w.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "W" in word:
                indices = [i for i, letter in enumerate(word) if letter == "W"]
                for index in indices:
                    word_as_list[index] = "W"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_w.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def x_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "X" not in word:
                btn_x.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "X" in word:
                indices = [i for i, letter in enumerate(word) if letter == "X"]
                for index in indices:
                    word_as_list[index] = "X"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_x.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def y_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "Y" not in word:
                btn_y.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "Y" in word:
                indices = [i for i, letter in enumerate(word) if letter == "Y"]
                for index in indices:
                    word_as_list[index] = "Y"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_y.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

    def z_btn():
        global tries
        global dashes
        global guessed
        while not guessed and tries > 0:
            word_as_list = list(dashes)
            if "Z" not in word:
                btn_z.destroy()
                tries -= 1
                printTries.configure(text=f"You have {tries} tries left.", font=("Arial", 20))
                show_hang()
                check_game_lost()
                break
            elif "Z" in word:
                indices = [i for i, letter in enumerate(word) if letter == "Z"]
                for index in indices:
                    word_as_list[index] = "Z"
                dashes = "".join(word_as_list)
                if "-" not in dashes:
                    guessed = True
                btn_z.destroy()
                printDashes.configure(text=dashes, font=("Arial", 30))
                show_hang()
                check_game_lost()
                break

# Button placements in GUI
    btn_a = Button(game, text='A', width=12, command=a_btn)
    btn_a.place(x=0, y=680)
    btn_b = Button(game, text='B', width=12, command=b_btn)
    btn_b.place(x=a, y=680)
    btn_c = Button(game, text='C', width=12, command=c_btn)
    btn_c.place(x=a*2, y=680)
    btn_d = Button(game, text='D', width=12, command=d_btn)
    btn_d.place(x=a*3, y=680)
    btn_e = Button(game, text='E', width=12, command=e_btn)
    btn_e.place(x=a*4, y=680)
    btn_f = Button(game, text='F', width=12, command=f_btn)
    btn_f.place(x=a*5, y=680)
    btn_g = Button(game, text='G', width=12, command=g_btn)
    btn_g.place(x=a*6, y=680)
    btn_h = Button(game, text='H', width=12, command=h_btn)
    btn_h.place(x=a*7, y=680)
    btn_i = Button(game, text='I', width=12, command=i_btn)
    btn_i.place(x=a*8, y=680)
    btn_j = Button(game, text='J', width=12, command=j_btn)
    btn_j.place(x=a*9, y=680)
    btn_k = Button(game, text='K', width=12, command=k_btn)
    btn_k.place(x=a*10, y=680)
    btn_l = Button(game, text='L', width=12, command=l_btn)
    btn_l.place(x=a*11, y=680)
    btn_m = Button(game, text='M', width=12, command=m_btn)
    btn_m.place(x=a*12, y=680)
    btn_n = Button(game, text='N', width=12, command=n_btn)
    btn_n.place(x=0, y=710)
    btn_o = Button(game, text='O', width=12, command=o_btn)
    btn_o.place(x=a, y=710)
    btn_p = Button(game, text='P', width=12, command=p_btn)
    btn_p.place(x=a*2, y=710)
    btn_q = Button(game, text='Q', width=12, command=q_btn)
    btn_q.place(x=a*3, y=710)
    btn_r = Button(game, text='R', width=12, command=r_btn)
    btn_r.place(x=a*4, y=710)
    btn_s = Button(game, text='S', width=12, command=s_btn)
    btn_s.place(x=a*5, y=710)
    btn_t = Button(game, text='T', width=12, command=t_btn)
    btn_t.place(x=a*6, y=710)
    btn_u = Button(game, text='U', width=12, command=u_btn)
    btn_u.place(x=a*7, y=710)
    btn_v = Button(game, text='V', width=12, command=v_btn)
    btn_v.place(x=a*8, y=710)
    btn_w = Button(game, text='W', width=12, command=w_btn)
    btn_w.place(x=a*9, y=710)
    btn_x = Button(game, text='X', width=12, command=x_btn)
    btn_x.place(x=a*10, y=710)
    btn_y = Button(game, text='Y', width=12, command=y_btn)
    btn_y.place(x=a*11, y=710)
    btn_z = Button(game, text='Z', width=12, command=z_btn)
    btn_z.place(x=a*12, y=710)

    game.mainloop()


# Calling the main func
main_game()