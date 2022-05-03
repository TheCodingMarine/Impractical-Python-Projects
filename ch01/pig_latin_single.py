vowels = ['a', 'e', 'i', 'o', 'u']

while True:

    word = input('Please enter a word: ').lower()

    if word[0] in vowels:
        new_word = word + 'way'
    else:
        letter = word[0]
        slice_word = word[1:]
        new_word = slice_word + letter + 'ay'

    print("\n{}".format(new_word))
