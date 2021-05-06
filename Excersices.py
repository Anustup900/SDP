#Write a function that takes in a person's name, and prints out a greeting.
#The greeting must be at least three lines, and the person's name must be in each line

def greet(person_name):
    print('Good Evening %s'%person_name)
    print('Thanks for joining here\nThanks for your effort in this project')
greet('Ajay')

#Use your function to greet at least three different people.
#Bonus: Store your three people in a list, and call your function from a for loop.

def greet(person):
        print('Goood Morning ',person)
greet('Ram')
greet('Syam')
greet('Aahin')

#Write a function that takes in a first name and a last name, and prints out a nicely formatted full name, in a sentence. Your sentence could be as simple as, "Hello, full_name."
#Call your function three times, with a different name each time.

def full_name(first_name,last_name):
    print("Hello ",first_name,last_name)
    
full_name('Kethuri','Ajay')
full_name('Vupputi','Bharath')
full_name('Goli','Vivek')

#Write a function that takes in two numbers, and adds them together. Make your function print out a sentence showing the two numbers, and the result.
#Call your function with three different sets of numbers.

def adder(num1,num2):
    sum=num1+num2
    print("Result of",num1,'and',num2,'is',sum)
    
adder(1,2)
adder(8,6)
adder(7,8)

#Write a function that takes two arguments, a person's name and their favorite color. The function should print out a statement such as "Hillary's favorite color is blue."
#Call your function three times, with a different person and color each time.

def favor(personame,color):
    print(personame,'favorite color is',color)
    
favor("Ajay's",'blue')
favor("Vikas's",'green')
favor("Vivek's",'black')

#Write a function that takes two arguments, a brand of phone and a model name. The function should print out a phrase such as "iPhone 6 Plus".
#Call your function three times, with a different combination of brand and model each time.

def argu(brand,model):
    print(brand,model)
    
argu('Redmi','Note 10')
argu('Iphone','11pro')
argu('Samsung','Galaxy M31S')

#Write a function that takes in two arguments, the name of a city and the name of a sports team from that city.
#Call your function three times, using a mix of positional and keyword arguments.

def describe(city,sport):
    print(city,"-",sport)
describe('Hyderabad','Cricket')
describe('Bangolore','Football')
describe('Jaipur','Kabbadi')

#Write a function that takes in two arguments, the name of a country and a major language spoken there.
#Call your function three times, using a mix of positional and keyword arguments.

def argu(country,languague):
    print('Country= ',country,',Major Languague= ',languague)
    
argu('India','Hindi')
argu('USA','English')
argu('Spain','Spanish')

#Store the values 'python', 'c', and 'java' in a list. Print each of these values out, using their position in the list.

language=['python','c','java']

print(language[0].title())
print(language[1].title())
print(language[2].title())

#Store the values 'python', 'c', and 'java' in a list. Print a statement about each of these values, using their position in the list.
#Your statement could simply be, 'A nice programming language is value.'


languages=['python','c','java']

for language in languages:

    print("A nice programming language is value "+language.title())
    
#Think of something you can store in a list. Make a list with three or four items, and then print a message that includes at least one item from your list. Your sentence could be as simple as, "One item in my list is a __."

cars=['Audi','hyundai','honda','toyota']

for car in cars:
    print('One item in my list is a ',car.title())
    
#Repeat First List, but this time use a loop to print out each value in the list.

mobiles=['redmi','iphone','samsung','vivo']

for mobile in (mobiles):
    
    print(" Mobile: " + mobile.title())
    
#Repeat First Neat List, but this time use a loop to print out your statements. Make sure you are writing the same sentence for all values in your list. Loops are not effective when you are trying to generate different output for each value in your list.

mobiles=['redmi','iphone','samsung','vivo']

for mobile in (mobiles):
    
    print(" Mobile: " + mobile.title())
    print('This is one of the top mobile in india')
    
#Repeat First Neat List, but this time use a loop to print out your statements. Make sure you are writing the same sentence for all values in your list. Loops are not effective when you are trying to generate different output for each value in your list.

mobiles=["redmi","iphone","samsung","vivo"]

for index, mobile in enumerate(mobiles):
    place = str(index)
    
    print("Place: " + place + " Mobile: " + mobile.title())
    print('This is the top brand mobile phone in India')
    
#Make a list that includes four careers, such as 'programmer' and 'truck driver'.
#Use the list.index() function to find the index of one career in your list.
#Use the in function to show that this career is in your list.
#Use the append() function to add a new career to your list.
#Use the insert() function to add a new career at the beginning of the list.
#Use a loop to show all the careers in your list.

careers=['programmer','gammer','driver','officer']

careers.append('leader')
careers.insert(0,'doctor')

for index,career in  enumerate(careers):
    place=str(index+1)
    print('place:'+place,'Job:',career.title())
    
#Create the list you ended up with in Working List, but this time start your file with an empty list and fill it up using append() statements.
#Print a statement that tells us what the first career you thought of was.
#Print a statement that tells us what the last career you thought of was.

careers=[]
careers.append('engineer')
careers.append('doctor')
careers.append('programmer')
careers.append('gammer')

print('First career i thought of '+careers[0].title())

print('Last career i thought of '+careers[3].title())

#Start with the list you created in Working List.
#You are going to print out the list in a number of different orders.
#Each time you print the list, use a for loop rather than printing the raw list.
#Print a message each time telling us what order we should see the list in.
#Print the list in its original order.
#Print the list in alphabetical order.
#Print the list in its original order.
#Print the list in reverse alphabetical order.
#Print the list in its original order.
#Print the list in the reverse order from what it started.
#Print the list in its original order
#Permanently sort the list in alphabetical order, and then print it out.
#Permanently sort the list in reverse alphabetical order, and then print it out.

careers=['programmer','gammer','driver','officer']

for career in careers:
    print('Job :',career.title())
    
for career in sorted(careers):
    print('Job : ',career.title())
    
for career in careers:
    print('Job :',career.title())
    
for career in sorted(careers,reverse=True):
    print('Job :',career.title())

for career in careers:
    print('Job :',career.title())
    
careers.sort()
for career in careers:
    print('Job:',career.title())
 
careers=['programmer','gammer','driver','officer']

for career in careers:
    careers.sort(reverse=True)
    print('Job :',career.title())
    
#Make a list of 5 numbers, in a random order.
#You are going to print out the list in a number of different orders.
#Each time you print the list, use a for loop rather than printing the raw list.
#Print a message each time telling us what order we should see the list in.
#Print the numbers in the original order.
#Print the numbers in increasing order.
#Print the numbers in the original order.
#Print the numbers in decreasing order.
#Print the numbers in their original order.
#Print the numbers in the reverse order from how they started.
#Print the numbers in the original order.
#Permanently sort the numbers in increasing order, and then print them out.
#Permanently sort the numbers in descreasing order, and then print them out.

numbers=[10,2,8,4]

print('Original Order\n')

for number in numbers:
    print(number)
    
print("Here the numbers in increasing order")
    
for number in sorted(numbers):
    print(number)
    
print('Here the numbers in the original order')

for number in numbers:
    print(number)

print('Here the numbers in decreasing order')

for number in sorted(numbers,reverse=True):
    print(number)
    
print('Here the numbers in the original order')

for number in numbers:
    print(number)


print('Permanently sort the numbers in increasing order, and then print them out')

for number in numbers:
    numbers.sort()
    print(number)
    
numbers=[10,2,8,4]
    
print('Permanently sort the numbers in descreasing order')

for number in numbers:
    numbers.sort(reverse=True)
    print(number)

#Copy two or three of the lists you made from the previous exercises, or make up two or three new lists.
#Print out a series of statements that tell us how long each list is.

careers=['programmer','gammer','driver','officer']
a=len(careers)
print('length of careers -',a)
cars=['Audi','hyundai','honda','toyota','telsa']
b=len(cars)
print('length of cars -',b)
language=['python','c','java']
c=len(language)
print('length of language -',c)

#Make a list that includes the names of four famous people.
#Remove each person from the list, one at a time, using each of the four methods we have just seen:
#Pop the last item from the list, and pop any item except the last item.
#Remove one item by its position, and one item by its value.
#Print out a message that there are no famous people left in your list, and print your list to prove that it is empty.

names=['sushant','anupama','ntr','naveen']

a=names.remove('ntr')
b=names.remove('sushant')
c=names.remove('naveen')
d=names.remove('anupama')



names=['sushant','anupama','ntr','naveen']

e=names.pop()

f=names.pop(0)

del names[3]

a=names.remove('ntr')
b=names.remove('sushant')
c=names.remove('naveen')
d=names.remove('anupama')

#Store the first ten letters of the alphabet in a list.
#Use a slice to print out the first three letters of the alphabet.
#Use a slice to print out any three letters from the middle of your list.
#Use a slice to print out the letters from any point in the middle of your list, to the end.

letters=['c','o','n','c','l','u','s','i','o','n']

first_three=letters[0:3]

for three_letters in first_three:
    print(three_letters)
    
any_three=letters[4:7]

for c in any_three:
    print(c)

last_letters=letters[7:11]

for a in last_letters:
    print(a)
    

#Your goal in this exercise is to prove that copying a list protects the original list.
#Make a list with three people's names in it.
#Use a slice to make a copy of the entire list.
#Add at least two new names to the new copy of the list.
#Make a loop that prints out all of the names in the original list, along with a message that this is the original list.
#Make a loop that prints out all of the names in the copied list, along with a message that this is the copied list.
   
names=['ajay','uday','vijay']

copied_list=names[:]

print('all of the names in the original list :')
a=copied_list

for a in copied_list:
    print(a)

print('all of the names in the copied list :')
copied_list.append('vikas')
copied_list.append('vivek')

for b in copied_list:
    print(b)


#Use the range() function to store the first twenty numbers (1-20) in a list, and print them out.

for number in range(1,21):
    print(number)
   
T#ake the first_twenty.py program you just wrote. Change your end number to a much larger number. How long does it take your computer to print out the first million numbers? (Most people will never see a million numbers scroll before their eyes. You can now see this!)


for number in range(1,1000000):
    print(number)


#Make a list of the first ten multiples of ten (10, 20, 30... 90, 100). There are a number of ways to do this, but try to do it using a list comprehension. Print out your list.

multiples=[]

for number in range(1,11):
    ten_mul=number*10
    multiples.append(ten_mul)
    
for multiple in multiples:
    
    print(multiple)
    
#We saw how to make a list of the first ten squares. Make a list of the first ten cubes (1, 8, 27... 1000) using a list comprehension, and print them out.
 
cubes=[]

for number in range(1,11):
    
    cubes.append(number**3)
    
for cube in cubes:
    print(cube)
    

#Store five names in a list. Make a second list that adds the phrase "is awesome!" to each name, using a list comprehension. Print out the awesome version of the names.

names=['pizza','Burger','tikka']

real_names=[]

for name in names:
    real_names.append(name.title()+" is awesome")
    
for real_name in real_names:
    print(real_name)


#Write out the following code without using a list comprehension:

plus_thirteen = [number + 13 for number in range(1,11)]
      
numbers=[1]

for number in range(1,11):
    
    print(number+13)
    
#Store a single sentence in a variable. Use a for loop to print each character from your sentence on a separate line.
    
sentence="I like to play pubg and cricket"

full=sentence.split(' ')

for sentence in full:
    print(sentence)
    
#Store a single sentence in a variable. Create a list from your sentence. Print your raw list (don't use a loop, just print the list).
    
  
sentence="I like to play pubg and cricket"

full=sentence.split(' ')

print(full)

#Store a sentence in a variable. Using slices, print out the first five characters, any five consecutive characters from the middle of the sentence, and the last five characters of the sentence.

sentence="I like to play cricket and pubg"

message=sentence[0:6]
print(message)

message=sentence[15:22]
print(message)

message=sentence[26:31]

print(message)

#Store a sentence in a variable, making sure you use the word Python at least twice in the sentence.
#Use the in keyword to prove that the word Python is actually in the sentence.
#Use the find() function to show where the word Python first appears in the sentence.
#Use the rfind() function to show the last place Python appears in the sentence.
#Use the count() function to show how many times the word Python appears in your sentence.
#Use the split() function to break your sentence into a list of words. Print the raw list, and use a loop to print each word on its own line.
#Use the replace() function to change Python to Ruby in your sentence.

sentence="python is a easy language,python is a high level language"

word= 'python' in sentence

print(word)

word=sentence.find('python')
print(word)

word=sentence.rfind('python')
print(word)

word=sentence.count('python')
print(word)

word=sentence.split(' ')
print(word)

word=sentence.replace('python','Ruby')
print(word)

#Store the possible scores a gymnast can earn from one judge in a tuple.
#Print out the sentence, "The lowest possible score is ___, and the highest possible score is ___." Use the values from your tuple.
#Print out a series of sentences, "A judge can give a gymnast ___ points."
#Don't worry if your first sentence reads "A judge can give a gymnast 1 points."
#However, you get 1000 bonus internet points if you can use a for loop, and have correct grammar.

scores=(1,2,3,4,5,6,7,8,9,10)

print('The lowest possible score is ',(scores[0]))

print('The highest possible score is ',(scores[9]))

print('A judge can give a gymnast',scores[7],'points')

    
    







