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

# working list
list = ['programmer', 'data analyst', 'app developer', 'full stack developer']
print(list.index('app developer'))
value = 'programmer'
print(value in list)
list.append('debugger')
list.insert(0, 'dba')
for i in list:
    print(i)

# starting from empty
list = []
list.append('programmer')
list.append('data analyst')
list.append('app developer')
list.append('full stack developer')
list.append('debugger')
list.append('DBA')
print('First career you thought of was- '+list[0])
print('Last career you thought of was- '+list[len(list)-1])


# ordered working list
list = ['programmer', 'data analyst', 'app developer', 'full stack developer']

print('the list in its original order.')
for item in list:
    print(item)
print('the list in alphabetical order.')
for item in sorted(list):
    print(item)

print('the list in its original order.')
for item in list:
    print(item)
print('the list in its reverse alphabetical order.')
for item in sorted(list, reverse=True):
    print(item)

print('the list in its original order.')
for item in list:
    print(item)
print('the list in its reverse order from what it started.')
list.reverse()
for item in list:
    print(item)

print('the list in its original order.')
list.reverse()
for item in list:
    print(item)
print('Permanently sorting the list in alphabetical order.')
list.sort()
for item in list:
    print(item)
print('Permanently sorting the list in reverse alphabetical order.')
list.sort(reverse=True)
for item in list:
    print(item)

    
# ordered numbers
list = [34, 67, 21, 98, 11]

print('the numbers in the original order.')
for item in list:
    print(item)
print('the numbers the increasing order.')
for item in sorted(list):
    print(item)

print('the numbers in the original order.')
for item in list:
    print(item)
print('the numbers in the decreasing order.')
for item in sorted(list, reverse=True):
    print(item)

print('the numbers in the original order.')
for item in list:
    print(item)
print('the numbers in the reverse order from what they started.')
list.reverse()
for item in list:
    print(item)

print('the numbers in the original order.')
list.reverse()
for item in list:
    print(item)
print('Permanently sorting the numbers in increasing order.')
list.sort()
for item in list:
    print(item)
print('Permanently sorting the numbers in decreasing order.')
list.sort(reverse=True)
for item in list:
    print(item)


# list lengths
list1 = ['Umesh', 'Singh', 'Learning', 'Python', 'Programming']
list2 = [34, 67, 21, 98, 11, 55, 21]
list3 = ['programmer', 'data analyst', 'app developer', 'full stack developer', 'debugger', 'DBA']
list4 = ['Python', 'Artificial Intelligence', 51, 'Machine Learning', 21, 'Deep Learning']

print('Items in list1- ', len(list1))
print('Items in list2- ', len(list2))
print('Items in list3- ', len(list3))
print('Items in list4- ', len(list4))


# famous people
people = ['Elon Musk', 'Bill Gates', 'Jeff Bezos', 'Steve Jobs']
people.pop()
people.pop(1)
del people[0]
people.remove('Jeff Bezos')
print('There is no famous people left in your list.')
print(people)
