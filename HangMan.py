import random


HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
                        
def game():
    guessing_words = ["ability","absence","academy","account","accused","achieve"]
    word = random.choice(guessing_words)
    if word == guessing_words[0]:
        print("the word denotes the strength to do something")
    elif word == guessing_words[1]:
        print("the word means to be hidden from something")
    elif word == guessing_words[2]:
        print("the denotes a educational facility")
    elif word == guessing_words[3]:
        print("the word denotes a ledger of someone")
    elif word == guessing_words[4]:
        print("the word denotes someone alleged")
    elif word == guessing_words[5]:
        print("a synononym of accomplish")
    else: 
        pass
    
    letters_list = []
    for i in word:
        letters_list.append(i)
    
    your_guess = ['_'] * len(word)
    chances = 0 
    print(HANGMAN_PICS[len(HANGMAN_PICS) - 1])
    print("welcome to hangman ", your_guess)
    Correct = []
    while your_guess != Correct:
        if '_' not in your_guess:
            print("you have guessed everything correctly")
            print("Thanks for playing with us have a good day !")
            break
        choose = input("please choose a character : ")
        chances += 1
        if choose in word and choose not in your_guess:
            index = word.find(choose)
            your_guess[index] = choose
            Correct.append("congratulations")
            print("Keep going")
            print(HANGMAN_PICS[len(HANGMAN_PICS) - len(Correct) - 1])
            print(your_guess)
        elif choose in word and choose in your_guess and your_guess.count(choose) <= letters_list.count(choose):
            index2 = word.rfind(choose)
            your_guess[index2] = choose
            letters = []
            print("Keep going")
            print(HANGMAN_PICS[len(HANGMAN_PICS) - len(Correct) - 1])
            print(your_guess)
        elif choose in word and choose in your_guess and your_guess.count(choose) > letters_list.count(choose):
            print("You have already chosen this character please !")
            print(HANGMAN_PICS[len(HANGMAN_PICS) - len(Correct) - 1])
            print(your_guess)
        else:
            print("you have made a mistake please try again")
            print(HANGMAN_PICS[len(HANGMAN_PICS) - len(Correct) - 1])
            print(your_guess)
            continue
        if len(Correct) == 3:
            print("you only have a few letters to go!")


        if len(Correct) == 5:
            print("you only have one to go !")


        if chances == 5:
            print("you have only 5 chances left keep going !!")
        if chances > 10:
            print("You have had so many tries please try again !!!!!")
            break


        


game()
