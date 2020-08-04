import random
from WordList import Words


def display_hangman(tries):
    stages = [
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # Sixth Try
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # Fifth Try
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # Fourth Try
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # Third Try
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # Second Try
        """
                   --------
                   |      |
                   |      O
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
    return stages[tries]


def get_random_word():
    word = random.choice(Words)
    return word.upper()


def get_user_name(name_1):
    print("Let's Play Hangman " + name_1, "\n", "Guess A Letter")
    return name_1


def main_game(word):
    dashes = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    name_1 = input("What Is Your Name: ")
    get_user_name(name_1)
    print(display_hangman(tries))
    print(dashes)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess A Letter or Word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                print(f"You have {tries} tries left")
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(dashes)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                dashes = "".join(word_as_list)
                if "_" not in dashes:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                print(f"You have {tries} tries left")
                guessed_words.append(guess)
            else:
                guessed = True
                dashes = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(dashes)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("You ran out of tries. The word was " + word + ". Better luck next time!")


def main():
    word = get_random_word()
    main_game(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_random_word()
        main_game(word)


if __name__ == "__main__":
    main()
