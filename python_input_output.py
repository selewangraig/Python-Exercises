#accept input from user
def take_input():
    word = input("Input Word: ")
    return word


#main function to print out only characters at even indices
def give_output(word):
    string = word
    
    print("Original string is: %s " % string)
    print("Prints out only characters in even index")

    for char in string[0::2]:
        print(char)

#call the functions
user_input = take_input()
give_output(user_input)