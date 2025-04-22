import random 
secret_food_words = ["vermicelli", "pastry", "cocoa", "custard"]


def gamefunc():
    food = random.choice(secret_food_words)
    your_guesses = ['_'] * len(food)
    print('choose a character {}'.format(your_guesses))
    chances = 0 
    hangman_index = 8
    while chances <= len(food) + 3: ## give the user 3 extra chances 
        chances += 1
        food
        guess = input("choose a character : ")
        if guess in food and guess not in your_guesses:
            index = food.find(guess)
            your_guesses[index] = guess


        elif guess in food and guess in your_guesses:
            index2 = food.rfind(guess) ## r find stands for reverse find, this is a very useful method and we will see why
            your_guesses[index2] = guess
        elif chances > 4 and your_guesses.count('_') >= 1:
            your_guesses[random.choice[food]]
        else:
            print("sorry try again your character was not in the string")


        if '_' not in your_guesses:
            print("your_guesses/n congratulations you have guessed all the letters correctly")


            


        print(your_guesses)
        
