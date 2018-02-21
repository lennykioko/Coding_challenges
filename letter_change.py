def letter_change(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_string = ""
    for char in string:
        if char in alphabet:
            if char == 'z':
                char = 'A'
                new_string += char
            else:
                index = string.find(char)
                index += 1
                char = alphabet[index] 
                if char in "aeiou":
                    char = char.upper()
                    new_string += char
                else:
                    new_string += char
    
    print(new_string)

letter_change('abcd')
letter_change('this is a beautiful day')
letter_change("abcdefghijklmnopqrstuvwxyz")

# alternative solution
def letter_change_2(string): 
    newString = ""
    
    for char in string:
        if char.isalpha():
            if char.lower() == 'z':
                char = 'a'
            else:
                char = chr(ord(char) + 1)

            if char in 'aeiou':
                char = char.upper()
            
            newString = newString + char

    return newString
    
letter_change('abcd')
letter_change('this is a beautiful day')
letter_change("abcdefghijklmnopqrstuvwxyz")
