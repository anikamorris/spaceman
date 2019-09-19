import unittest

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # loop through each letter of secret_word, if all letters are in letters_guessed, return True, else return False
    for i in range(len(secret_word)):
        if not (secret_word[i] in letters_guessed):
            return False
    return True
    
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

class GuessWordsTest(unittest.TestCase):
    # This is the function we have written to automatically test the sum function
    def test_is_word_guessed(self):
        # Test functions usually contain contain several assertion statements, and
        # each has a condition that must be true. If not, then an error is thrown.
        # This is the general format commonly used for most assertion statements
        # assert function(input_data) == expected_result

        # An optional helpful error message can be included after the condition
        # assert function(input_data) == expected_result, "Helpful error message"

        # These are some assertions that test the correctness of the sum function
        self.assertEqual(is_word_guessed('apple', ['a', 'p', 'e', 'l']), True)
        self.assertEqual(is_word_guessed('bored', ['a', 'c', 'o']), False)
        self.assertEqual(is_word_guessed('bored', ['b', 'o', 'r', 'e', 'd']), True)
        self.assertEqual(is_word_guessed('banana', ['b', 'a', 'n']), True)
        self.assertEqual(is_word_guessed('nothing', []), False)

    def test_is_guess_in_word(self):
        self.assertEqual(is_guess_in_word('$', 'camera'), False)
        self.assertEqual(is_guess_in_word('l', 'maybe'), False)
        self.assertEqual(is_guess_in_word('r', 'ready'), True)
        self.assertEqual(is_guess_in_word(' ', 'humble'), False)
        self.assertEqual(is_guess_in_word('f', 'flower'), True)

    def test_has_been_guessed(self):
        self.assertEqual(has_been_guessed('b', ['m', 'q', 'r', 'l', 'o']), False)
        self.assertEqual(has_been_guessed('c', ['l', 'n', 'i', 'c']), True)
        self.assertEqual(has_been_guessed('4', ['m', 'q', 'r', 'l', 'o']), False)
        self.assertEqual(has_been_guessed('*', ['l', 'n', 'i', 'c']), False)
        self.assertEqual(has_been_guessed(' ', ['a', 'p', 'e', 'l']), False)
    
if __name__ == "__main__":
    # Run the test function
    unittest.main()
    # GuessWordsTest.test_is_word_guessed()
    