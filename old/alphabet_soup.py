def alphabet_soup(string):
    string = list(string)
    string = sorted(string)
    new_string = "".join(string)

    return new_string

print(alphabet_soup("coderbyte is awesome and epic"))
