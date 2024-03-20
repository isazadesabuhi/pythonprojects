def word_replace():
    phrase = "My name is Sabuhi."
    word_to_replace = input("Which word do you want to change? ")
    word_replacement = input("To which word do you want to change? ")
    print(phrase.replace(word_to_replace, word_replacement))
    
word_replace()