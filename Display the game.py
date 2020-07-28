import random
from hangMan import display_hangman
from WordList import Words
from tkinter import *

game = Tk()
game.title("HangMan")
game.geometry('1280x720')

welcome = Label(game, text="Please Enter Your Name")
welcome.grid(column=5, row=1, pady=7)

name = Entry(game, width=10)
name.grid(column=5, row=3, pady=7)


def name_submitted():
    if name.get().isalpha():
        msg = Label(game, text="Let's Play HangMan " + name.get())
        msg.grid(column=5, row=3)
        name_bt.destroy()
    else:
        msg_1 = Label(game, text="Please Enter A Valid Name")
        msg_1.grid(column=6, row=3)
        

def get_random_word():
    word = random.choice(Words)
    return word.upper()


name_bt = Button(game, text='Submit', width=8, command=name_submitted)
name_bt.grid(column=5, row=6)


def game_logic(word):
    dashes = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    hangman = Label(game, text=display_hangman(tries))
    hangman.grid(column=8, row=3, rowspan=3, columnspan=3)

    print_dashes = Label(game, text=dashes)
    print_dashes.grid(column=5, row=3)

    while not guessed and tries > 0:
        guess_box = Entry(game, width=4)
        guess = guess_box.get().upper()
        letter_submit_button = Button(game, text="Submit", command=guess_box.get())
        letter_submit_button.grid(column=5, row=4)
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                already_guessed = Label(game, text=f"You Already Guessed {guess} Letter")
                already_guessed.grid(column=5, row=5)
            elif guess not in word:
                wrong_guess = Label(game, text=f"{guess} is not in the word")
                wrong_guess.grid(column=5, row=5)
                tries -= 1
                hangman = Label(game, text=display_hangman(tries))
                hangman.grid(column=8, row=3, rowspan=3, columnspan=3)
                guessed_letters.append(guess)
            else:
                correct_guess = Label(game, text=f"Bravo!! {guess} is in the word")
                correct_guess.grid(column=5, row=5)
                guessed_letters.append(guess)
                word_as_list = list(guess)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index]=guess
                    dashes = "".join(word_as_list)
                    if "_" not in dashes:
                        guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                already_guessed = Label(game, text=f"You Already Guessed {guess} Word")
                already_guessed.grid(column=5, row=5)
            elif guess != word:
                wrong_guess = Label(game, text=f"{guess} is not word")
                wrong_guess.grid(column=5, row=5)
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                dashes = word
        else:
            invalid_guess = Label(game, text="Not A Valid Guess")
            invalid_guess.grid(column=5, row=5)
        print_dashes = Label(game, text=dashes)
        print_dashes.grid(column=5, row=3)
    if guessed:
        congrats = Label(game, text="Congrats, you guessed the word! You win!")
        congrats.grid(column=5, row=10)
    else:
        failed = Label(game, text=f"You ran out of tries. The word was {word} Better luck next time!")
        failed.grid(column=5, row=10)


def main():
    word = get_random_word()
    game_logic(word)
    play_again = Entry(game, width=4)
    play_again.grid(column=5, row=5)

    play_button = Button(game, text="Y/N")
    play_button.grid(column=5, row=6)
    while play_again.get().upper() == "Y":
        word = get_random_word()
        game_logic(word)


game.mainloop()


if __name__ == "__main__":
    main()


