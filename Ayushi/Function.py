def greet(name):
    print("hello %s !"%name)
    print("Its lovely meeting you %s"%name)
    print("%s Can u come over for dinner?"%name)
mylist={'Amay','bron','carry'}
for i in mylist:
    greet(i)
    
    
    def fullname(fname,lname):
    name=fname.capitalize()+' '+lname.capitalize()
    print("Hello %s" %name)
fullname('Ayushi','Chauhan')
fullname('bron','elark')
fullname('shon','mendez')


def cal(n1,n2):
    sum=n1+n2
    print("sum=%d"%sum)
cal(100,1)
cal(20,10)
cal(200,23)


def mcal(n1,n2):
    sum=n1+n2
    return sum
s=mcal(2,3)
print("sum=%d"%s)
