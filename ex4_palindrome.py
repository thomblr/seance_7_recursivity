def clean_word(word):
    return str.lower(str.strip(str.replace(word, ' ', '')))


def is_palindrome(a_certain_word):
    a_certain_word = clean_word(a_certain_word)

    if a_certain_word == '':
        return True
    else:
        if a_certain_word[0] != a_certain_word[-1]:
            return False
        else:
            return is_palindrome(a_certain_word[1:-1])


print(is_palindrome('rue Verlaine gela le genial reveur'))
