def longest_word(sen): 

    word = ""
    words = []
    sen = sen.lower()
    sen += '.'
    for char in sen:
        if char in "abcdefghijklmnopqrstuvwxyz":
            word = word + char
        else:
            words.append(word)
            word = ""
        
    sizes = {}
    for word in words:
        sizes[word] = len(word)
    
    longest = max(sizes.values())
    for word, length in sizes.items():
        if longest == length:
            print("The longest word is {}".format(word))


longest_word('This is the guaranteed path to greatness and awesomeness as a software engineer')
longest_word("""The longest word in any of the major English language dictionaries is
               pneumonoultramicroscopicsilicovolcanoconiosis, yes; medically, it is the same as silicosis.""")
