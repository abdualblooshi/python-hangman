
# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    
    # letters_guessed = ['e', 'f', 'g', 'h', 'j']
    # if we join letters_guessed we get "efghj"
    # note: 
    # converting list to a string makes it easier
    # to compare lists with strings
    
    letters_guessed_string = ''.join(letters_guessed)
    for letter in secret_word:
      #print(letter) #for testing purposes
      #print(letters_guessed.count(letter)) # prints count
      if letters_guessed.count(letter) == 0:
        return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    letters_guessed_string = ''.join(letters_guessed)
    guessed_letters = [] # this will be a list of letters that have been correctly guessed
    for guess in secret_word: # this is a for loop that goes through each letter in secret_word
      if letters_guessed.count(guess) > 0: # this checks to see if the letter has been guessed
        guessed_letters.append(guess) # if it has been guessed, it is added to the list of guessed letters
      else:
        guessed_letters.append('_') # otherwise it will be just an underscore
    return ''.join(guessed_letters) # this joins the list of guessed letters into a string which gets returned
    #guessed_list = guessed_word.split('_')
    #return guessed_list



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    
    unused_letters = []
    alphabet = string.ascii_lowercase
    # alphabet = ['a','b','c','d','e','f'....] commented this because i could use string.ascii_lowercase instead
    letters_guessed_string = ''.join(letters_guessed)
    for letter in alphabet:
      if letters_guessed.count(letter) == 0: # if the letter is not in the alphabet then it is added to the unused letters list
        unused_letters.append(letter)
    return ''.join(unused_letters)
      
  
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    guesses_count = 6
    warnings_count = 3
    letters_guessed = []
    correct_guess = is_word_guessed(secret_word, letters_guessed)
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(guesses_count) + " letters long.")
    print("------------------------------------------------------")
    print("You have "+str(warnings_count)+" warnings left.")
    print("You have "+str(guesses_count)+" guesses left.")
    print("Available letters: "+get_available_letters(''))
    
    while not correct_guess:
      guess = input("Please guess a letter: ")
      guess = guess.lower()
      if ((guess in secret_word and guess not in letters_guessed) and len(guess) == 1):
        letters_guessed.append(guess)
        # print(letters_guessed) for debugging purposes
        print("Good guess: "+get_guessed_word(secret_word, letters_guessed))
        print("------------------------------------------------------")
        print("You have "+str(warnings_count)+" warnings left.")
        print("You have "+str(guesses_count)+" guesses left.")
        print("Available letters: "+get_available_letters(letters_guessed))
      else:
        if (guess in letters_guessed) and len(guess) == 1:
          print("Oops! You've already guessed that letter: "+get_guessed_word(secret_word, letters_guessed))
          print("------------------------------------------------------")
          print("You have "+str(guesses_count)+" guesses left.")
          print("Available letters: "+get_available_letters(letters_guessed))
        else:
          letters_guessed.append(guess)
          if (warnings_count > 0 and (not str.isalpha(guess))) and len(guess) > 1:
            warnings_count -= 1
            print("Oops! That is not a valid letter. You have "+str(warnings_count)+" warnings left: "+get_guessed_word(secret_word, letters_guessed))
            print("------------------------------------------------------")
            print("You have "+str(guesses_count)+" guesses left.")
            print("Available letters: "+get_available_letters(letters_guessed))
          else:
            guesses_count -= 1
            print("Oops! That letter is not in my word: "+get_guessed_word(secret_word, letters_guessed))
            print("------------------------------------------------------")
            print("You have "+str(guesses_count)+" guesses left.")
            print("Available letters: "+get_available_letters(letters_guessed))
      if is_word_guessed(secret_word, letters_guessed):
        print("------------------------------------------------------")
        print("Congratulations, you won!")
        print("Your total score for this game is: "+str(guesses_count*len(set(secret_word))))
        print("------------------------------------------------------")
        break
      elif guesses_count == 0:
        print("Sorry, you ran out of guesses. The word was "+secret_word+".")
        break

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    
    if len(my_word) != len(other_word): # this checks if the length of the two words are the same, otherwise it will just return false
      return False # returning false will avoid the program from appending unnecessary (fixes a bug that i faced)
    
    temp = []
    
    for x in range(0, len(my_word)):
      if my_word[x] != '_':
        temp.append(other_word[x])
        # temp.append(my_word[x])
        # print(my_word[x])
      else:
        temp.append('_')
        # print(my_word[x])
    if my_word == ''.join(temp):
      return True
    return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    matching_letters = []
    for word in wordlist:
      if match_with_gaps(my_word, word):
        matching_letters.append(word)
    #   print(matching_letters)
    if len(matching_letters) == 0:
      print("No matches found")
    return matching_letters



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    guesses_count = 6
    warnings_count = 3
    letters_guessed = []
    correct_guess = is_word_guessed(secret_word, letters_guessed)
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(guesses_count) + " letters long.")
    print("------------------------------------------------------")
    print("You have "+str(warnings_count)+" warnings left.")
    print("You have "+str(guesses_count)+" guesses left.")
    print("Available letters: "+get_available_letters(''))
    
    while not correct_guess:
      guess = input("Please guess a letter: ")
      guess = guess.lower()
      if ((guess in secret_word and guess not in letters_guessed) and len(guess) == 1):
        letters_guessed.append(guess)
        # print(letters_guessed) for debugging purposes
        print("Good guess: "+get_guessed_word(secret_word, letters_guessed))
        print("------------------------------------------------------")
        print("You have "+str(warnings_count)+" warnings left.")
        print("You have "+str(guesses_count)+" guesses left.")
        print("Available letters: "+get_available_letters(letters_guessed))
      else:
        if (guess in letters_guessed) and len(guess) == 1:
          print("Oops! You've already guessed that letter: "+get_guessed_word(secret_word, letters_guessed))
          print("------------------------------------------------------")
          print("You have "+str(guesses_count)+" guesses left.")
          print("Available letters: "+get_available_letters(letters_guessed))
        elif guess == "*":
          print("Possible matches are: ")
          print(*show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
          print("------------------------------------------------------")
          print("You have "+str(warnings_count)+" warnings left.")
          print("You have "+str(guesses_count)+" guesses left.")
          print("Available letters: "+get_available_letters(letters_guessed))
        else:
          letters_guessed.append(guess)
          if (warnings_count > 0 and (not str.isalpha(guess))) and len(guess) > 1:
            warnings_count -= 1
            print("Oops! That is not a valid letter. You have "+str(warnings_count)+" warnings left: "+get_guessed_word(secret_word, letters_guessed))
            print("------------------------------------------------------")
            print("You have "+str(guesses_count)+" guesses left.")
            print("Available letters: "+get_available_letters(letters_guessed))
          else:
            guesses_count -= 1
            print("Oops! That letter is not in my word: "+get_guessed_word(secret_word, letters_guessed))
            print("------------------------------------------------------")
            print("You have "+str(guesses_count)+" guesses left.")
            print("Available letters: "+get_available_letters(letters_guessed))
      if is_word_guessed(secret_word, letters_guessed):
        print("------------------------------------------------------")
        print("Congratulations, you won!")
        print("Your total score for this game is: "+str(guesses_count*len(set(secret_word))))
        print("------------------------------------------------------")
        break
      elif guesses_count == 0:
        print("Sorry, you ran out of guesses. The word was "+secret_word+".")
        break
      



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    #hangman(secret_word)
    # hangman("tact")
    hangman_with_hints("tact")

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
