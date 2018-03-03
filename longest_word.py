def longest_word(sen): 
    words = sen.split()
        
    sizes = {}
    for word in words:
        sizes[word] = len(word)
    
    longest = max(sizes.values())
    for word, length in sizes.items():
        if longest == length:
            print("The longest word is {}".format(word))


longest_word('Andela is fantastic')
longest_word("this is Andela.")
