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

# weight lifting
def dict_function():
    dictionary = {'Push-ups': '50', 'Squats': '25', 'Chest Press': '51', 'Pull-ups': '100'}
    print('\nPrinting the key-value pairs using for loop--')
    for i, j in dictionary.items():
        print('I did ' + j + ' ' + i)

    print('\nModifying one of the values--')
    dictionary['Pull-ups'] = '2 times, 100'
    for i, j in dictionary.items():
        print('I did ' + j + ' ' + i)

    print('\nAdding a new key-value pair--')
    dictionary['Deadlifts'] = '21'
    for i, j in dictionary.items():
        print('I did ' + j + ' ' + i)

    print('\nRemoving a key-value pair--')
    del dictionary['Squats']
    for i, j in dictionary.items():
        print('I did ' + j + ' ' + i)

dict_function()

# mountain heights
dict_mountains = {'Mount Everest': '8,848', 'K2': '8,611', 'Kangchenjunga': '8,586', 'Lhotse': '8,516', 'Makalu': '8,485'}
print("\nNames of tallest mountains in the world--")
for i in dict_mountains.keys():
    print(i)

print("\nElevation of tallest mountains in the world--")
for j in dict_mountains.values():
    print(j)

print("\nTallest Mountains in the world and their elevations--")
for i, j in dict_mountains.items():
    print(i + ' is ' + j + ' meters tall')

# mountains heights 2
dict_mountains = {'Mount Everest': '8,848', 'K2': '8,611', 'Kangchenjunga': '8,586', 'Lhotse': '8,516', 'Makalu': '8,485'}

print("\nTallest Mountains in the world and their elevations--")
for i, j in sorted(dict_mountains.items()):
    print(i + ' is ' + j + ' meters tall')

# mountain heights 3
dict_mountains = {'Mount Everest': ['8848', round(8848*3.28, 3)], 'K2': ['8611', round(8611*3.28, 3)], 'Kangchenjunga': ['8586', round(8586*3.28, 3)], 'Lhotse': ['8516', round(8516*3.28, 3)], 'Makalu': ['8485', round(8485*3.28, 3)]}
print("Names of tallest mountains in the world--")
for i in dict_mountains.keys():
    print(i)

print("\nElevation of tallest mountains in meters--")
for j in dict_mountains.values():
    print(j[0])

print("\nElevation of tallest mountains in feet--")
for j in dict_mountains.values():
    print(j[1])

print("\nTallest Mountains in the world and their elevations--")
for i, j in dict_mountains.items():
    print(i + ' is', j[0], 'meters tall, or', j[1], 'feet')

## bonus
def fun_feet(i):
    value = int(i)
    return round(value*3.28, 2)

lst = []
dict_mountains = {'Mount Everest': '8848', 'K2': '8611', 'Kangchenjunga': '8586', 'Lhotse': '8516', 'Makalu': '8485'}
for i in dict_mountains.values():
    value = fun_feet(i)
    lst.append(value)

# print(lst)
dict_mountains = {'Mount Everest': ['8848', lst[0]], 'K2': ['8611', lst[1]], 'Kangchenjunga': ['8586', lst[2]], 'Lhotse': ['8516', lst[3]], 'Makalu': ['8485', lst[4]]}
print(dict_mountains)


# mountain heights 4
dict_mountains = {'Mount Everest': {'elevation': '8848', 'range': 'himalaya'}, 'K2': {'elevation': '8611', 'range': 'karakoram'},
                  'Kangchenjunga': {'elevation': '8586', 'range': 'himalaya'}, 'Lhotse': {'elevation': '8516', 'range': 'himalaya'},
                  'Makalu': {'elevation': '8485', 'range': 'himalaya'}}
print('Name of Tallest Mountains--')
for i in dict_mountains.keys():
    print(i)

print('Elevation of Tallest Mountains--')
for i in dict_mountains.values():
    print(i['elevation'])

print('Range of Tallest Mountains--')
for i in dict_mountains.values():
    print(i['range'])

print('Details of Tallest Mountains--')
for i, j in dict_mountains.items():
    print(i, 'is an', j['elevation'], 'meter tall mountain in the', j['range'], 'range.')
