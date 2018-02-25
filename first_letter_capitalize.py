def first_letter_capitalize(string):
    new_string = ""
    words = string.split()

    for word in words:
        word = word.title()
        new_string += word + " "
    
    return new_string

print(first_letter_capitalize("good boy gone wild"))

# alternative solution (has some issues)
def first_letter_capitalize_2(string):
    string = string.split()
    for word in string:
        print(word[0].upper() + word[1::], end=" ")

first_letter_capitalize_2("good boy gone wild")
