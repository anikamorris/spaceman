import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for i in range(len(secret_word)):
        if not (secret_word[i] in letters_guessed):
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    guessed_word = []
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            guessed_word.append(secret_word[i])
        else:
            guessed_word.append("_")
    return "".join(guessed_word)


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    for i in range(len(secret_word)):
        if guess==secret_word[i]:
            return True
    return False

def has_been_guessed(guess, letters_guessed):
    return guess in letters_guessed


def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def round0(secret_word):
    length = str(len(secret_word))
    print('Welcome to Spaceman! \n The secret word contains ' + length + ' letters \n You have ' + length + ' guesses, please only enter 1 letter per round")

def game(secret_word):
    incorrect_guesses = len(secret_word)
    letters_guessed = []
    letters_not_guessed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    guessed_word = get_guessed_word(secret_word, letters_guessed)

    while guessed_word != secret_word and incorrect_guesses > 0:
        print("These letters haven't been guessed yet: " + "".join(letters_not_guessed))
        guess = user_input('Enter a lowercase letter: ')
        if len(guess) > 1:
            while len(guess) > 1:
                guess = user_input('Please only enter one letter at a time: ')

        has_been_guessed = has_been_guessed(guess, letters_guessed)
        while has_been_guessed:
            guess = user_input('You already guessed that letter, choose a different one: ')
            has_been_guessed = has_been_guessed(guess, letters_guessed)

            
        letters_guessed.append(guess)
        letters_not_guessed.remove(guess)
        if is_guess_in_word(guess, secret_word):
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print('Your guess appears in the word! \n Secret word so far: ' + guessed_word)
        else:
            incorrect_guesses -= 1
            print('Your guess was not in the word. Please try again \n You have ' + str(incorrect_guesses) + ' guesses left \n Secret word so far: ' + guessed_word)
        

def win_lose(secret_word):
    if is_word_guessed:
        print('You won! The secret word was ' + secret_word)
    else: 
        print('You lost :( The secret word was ' + secret_word)

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    round0(secret_word)
    game(secret_word)
    win_lose(secret_word)

# set secret word and start game
secret_word = load_word()
spaceman(secret_word)