def word_len(word):
    """Returns the length of word not counting spaces

    >>> word_len("a la carte")
    8
    >>> word_len("hello")
    5
    >>> word_len('')
    0
    >>> word_len("coup d'etat")
    10
    """
    return len(word.replace(" ", ""))


def has_no_e(word):
    """Returns True if word contains no e letter

    >>> has_no_e("hello")
    False
    >>> has_no_e("myopia")
    True
    """
    for i in word:
        if i == "e":
            return False
    return True


def avoids(word, forbidden):
    """Returns True if word does not contain any letter in forbidden string

    >>> avoids('yummy', 'abcdefg')
    True
    >>> avoids('dictionary', 'abcdefg')
    False
    >>> avoids('crypt', 'aeiou')
    True
    >>> avoids('tangible', 'aeiou')
    False
    """
    for i in word:
        if i in forbidden:
            return False
    return True


def uses_only(word, available):
    """Returns True if each of the letters in word is contained in string

    >>> uses_only('aloha', 'acefhlo')
    True
    >>> uses_only('flow', 'acefhlo')
    False
    >>> uses_only('pizza', 'enipaz')
    True
    >>> uses_only('pineapple', 'enipaz') 
    False
    >>> uses_only('spine', 'enipaz') 
    False
    """
    for i in word:
        if i not in available:
            return False

    return True


def uses_all(word, required):
    """Returns True if each of the letters in required is contained in word

    >>> uses_all('resampling', 'aeipn')
    True
    >>> uses_all('plenty', 'aeipn')
    False
    >>> uses_all('penalize', 'enipaz')
    True
    >>> uses_all('penalty', 'enipaz')
    False
    """
    for i in required:
        if i not in word:
            return False
    return True


def is_abecedarian(word):
    """Returns True if the letters in a word appear in alphabetical order

    >>> is_abecedarian('loop')
    True
    >>> is_abecedarian('almost')
    True
    >>> is_abecedarian('lopsided')
    False
    >>> is_abecedarian('always')
    False
    """
    s = ""
    a = list(word)
    a.sort()
    for i in a:
        s += i
    if s != word:
        return False

    return True
