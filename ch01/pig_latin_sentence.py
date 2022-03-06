vowels = ['a', 'e', 'i', 'o', 'u']

while True: 
    sentence = input('Please enter a sentence: ').split()
    new_sentence = []
    for word in sentence:
        if word[0] in vowels:
            new_word = word + 'way'
            new_sentence.append(new_word)
        else:
            letter = word[0]
            new_word = word[1: ] + letter + 'ay'
            new_sentence.append(new_word)

    full_sentence = ' '.join(new_sentence)
    print(full_sentence)
    
    keep_going = input("Would you like to enter another sentence? (y or n): ")
    if keep_going.lower() == 'n':
        break
