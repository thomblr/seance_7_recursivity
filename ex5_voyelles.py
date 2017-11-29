def count_vowels(a_certain_word, vowel, nb=0):
    """Returns the number of vowel in a certain word
    Parameters
    ----------
    a_certain_word: the word you want to count the vowel (str)
    vowel: the vowel you want to count (str)
    nb: the current nb of vowel in the word (int)

    Returns
    -------
    n: the number of vowel in the word (int)"""

    if a_certain_word == '':
        return nb
    else:
        if a_certain_word[0] == vowel:
            nb += 1
        return count_vowels(a_certain_word[1:], vowel, nb)


print(count_vowels('Thomas', 'o'))
