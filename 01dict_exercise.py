# dictionaries

# pet names
dictionary = {'ziggy': 'canary', 'Tommy': 'dog', 'Simba': 'lion', 'Mufasa': 'tiger'}
for i, j in dictionary.items():
    print(i+" is a "+j)

# polling friends
print('Who is your favourite person??')
dictionary = {'Singh': 'I like Elon Musk', 'Sharma': 'I like Bill Gates', 'Verma': 'I like Sundar Pichai', 'Mehta': 'I like Jeff Bezos'}
for i, j in dictionary.items():
     print(i+"'s  Response- "+j)

# pet names 2

def dict_fun():
    dictionary = {'Kittie': 'cat', 'Tommy': 'dog', 'Simba': 'lion', 'Mufasa': 'tiger'}
    for i, j in dictionary.items():
        print(i + " is a " + j)

    print('\nModifying one value--')
    dictionary['Kittie'] = 'cat. She is a Ragdoll breed.'
    for i, j in dictionary.items():
        print(i + ' is a ' + j)

    print('\nAdding a new key-value pair--')
    dictionary['Bald'] = 'eagle'
    for i, j in dictionary.items():
        print(i + " is a " + j)

    print('\nRemoving a key-value pair--')
    del dictionary['Bald']
    for i, j in dictionary.items():
        print(i + " is a " + j)

dict_fun()

