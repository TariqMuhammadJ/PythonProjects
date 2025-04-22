def password_checker():
    print("welcome to the password checker program")
    password = input("what is your password : ")
    correct_letters = ['_'] * len(password)
    index_positioning = -1 
    check = input("please re-type your password ")
    if len(check) > len(password) or len(check) < len(password):
        raise  Exception("sorry your password should be {} characters long".format(len(password))) ## so the two ways to break out of a function is to raise an exception and return none 
        
    for letter in check:
        index_positioning += 1 ## this will basically increment 1 time for each letter in check 
        if letter == password[index_positioning]:
            correct_letters[index_positioning] = letter
        elif letter not in check:
            continue
    if '_' not in correct_letters:
        print("you have successfully logged in") 
        print(correct_letters)
    else:
        print("these are the correct letters you have guessed")
        print(correct_letters)


    print("this is your password")
    print(correct_letters)



password_checker()
