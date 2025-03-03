#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    if word.find(letter) >=0:
        return True
    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    if letter == word[spot]:
        return True
    return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback = ""
    for spot in range (5):
        letter = myGuess[spot]
        if inSpot(letter, word, spot) == True:
            feedback = feedback + letter.upper()
        elif inWord(letter, word) == True:
            feedback = feedback = feedback + letter.lower()
        else:
            feedback = feedback + "*"
    return feedback


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    #print(todayWord)
    guess =""
    count = 0
    while guess != todayWord and count <6:
        goodGuess == False
        while goodGuess == False:
            guess = input("Enter Word: ")
            if guess in wordList:
                count = count + 1
                goodGuess = True
            else:
                print("Invalid Word:")
       
        feedback = rateGuess(guess, todayWord)
        print(feedback)
    if count < 6:
        print("YAY")
    else:
        print("Boo")

    print("The word was", todayWord)
    #User should get 6 guesses to guess

    #Ask user for their guess
    #Give feedback using on their word:





if __name__ == '__main__':
  main()
