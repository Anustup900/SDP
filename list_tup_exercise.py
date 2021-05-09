# lists_tuples

# first list
list = ['python', 'c', 'java']
print(list[0])
print(list[1])
print(list[2])

# first neat list
list = ['Python', 'C', 'Java']
print(list[0] + " is easy to learn.")
print(list[1] + " is good for beginners.")
print(list[2] + " is best for application development.")

# your first list
list = ['Python', 'AI', 'ML', 'DL']
print('One item in my list is ' + list[1])

# first list - loop
list = ['python', 'c', 'java']
for i in list:
    print(i)

# first neat list - loop
list = ['Python', 'C', 'Java']
for j in list:
    print(j + " is easy to learn.")
    print(j + " is good for beginners.")
    print(j + " is a programming language.")

# your first list - loop
list = ['Python', 'Artificial Intelligence', 'Machine Learning', 'Deep Learning']
for k in list:
    print('One item in my list is ' + k)

# ------------------------------------------------

# famous people
people = ['Elon Musk', 'Bill Gates', 'Jeff Bezos', 'Steve Jobs']
people.pop()
people.pop(1)
del people[0]
people.remove('Jeff Bezos')
print('There is no famous people left in your list.')
print(people)
