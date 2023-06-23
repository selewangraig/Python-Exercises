#create dictionary
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

#function to add item Jake to dictionary
def add_value():
    phonebook ["Jake"] = 938273443

#function to remove Jill
def remove_value():
    phonebook.pop("Jill")

#function to test code
def test_code():
    if "Jake" in phonebook:
        print("Jake is listed in the phonebook.")

    if "Jill" not in phonebook:
        print("Jill is not in the phonebook.")


#testing code
add_value()
remove_value()
test_code()
