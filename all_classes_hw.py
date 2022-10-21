'''
print('Hello World')
print ('This is my First Program')

#---------------------------------------------------------------

x=3
print ('Value is : ',x)

#---------------------------------------------------------------

x=6
y=4
print ('Sum is : ',x+y)

#---------------------------------------------------------------



x=int(input('Enter a value for x : '))
y=int(input('Enter a value for y : '))
sum=x+y
print('Sum is : ',sum)

#---------------------------------------------------------------


x=int(input('Enter a value for x : '))
y=int(input('Enter a value for y : '))
if (x>y):
    print('x is greater than y')
else:
    print('y is greater than x')


#---------------------------------------------------------------



#----------------for loop--------------
# .......... 1 to 100 addition.....
ans=0
for i in range(1,101,1):
    ans=ans+i
print('Sum is :',ans)

#--------------End--------------------------------

#----List----------------
mylist=['Hasan','Shahin','Bahar']
print(mylist)

print(mylist[2])


mylist.append('Ranga')
print('Append item to list : ', mylist)

mylist.remove(mylist[2])
print('Remove an item from list : ',mylist)


#-----------------Calculator----------------------------------------------
x=input("Enter a value for x : ")
y=input("Enter a value for y : ")

z=input("Options are (+-*/ or x for exit) : ")
while (z!=0):
  if (z=='+'):
    print(int(x)+int(y))
  elif(z=='-'):
    print(int(x)-int(y))
  elif(z=='*'):
    print(int(x)*int(y))
  elif(z=='/'):
    print(int(x)/int(y))
  elif (z=='x'):
    exit()
  z=input("Options are (+-*/ or x for exit) : ")  

  #---------------------------------------------------------------



                                #Python Operators

#---------------------------Python Logical Operators---------------------


# Operator 	    Description 	                                                Example 	
# and  	        Returns True if both statements are true 	                    x < 5 and  x < 10 	
# or 	            Returns True if one of the statements is true 	                x < 5 or x < 4 	
# not 	        Reverse the result, returns False if the result is true         not(x < 5 and x < 10)

#------------------------and operator------------
x=92

if x<60:
    print("Grade is : F")
elif x>=60 and x<70:
    print("Grade is : D")
elif x>=70 and x<80:
    print("Grade is : B")
elif x>=80 and x<90:
    print("Grade is : A")
elif x>=90 and x<=100:
    print("Grade is : A+")

#Grade is : A+

#------------------------or operator------------
y=90
print(y>50 or y>60)
#True

#------------------------not operator------------
y=90
print(not(y>50 or y>60))
#False

#---------------------------End of Logical Comparison Operators---------------------

#---------------------------Python Arithmetic Operators---------------------


# Operator 	Name 	            Example 	
# + 	        Addition 	           x + y 	
# - 	        Subtraction 	        x - y 	
# * 	        Multiplication 	        x * y 	
# / 	        Division 	            x / y 	
# % 	        Modulus 	            x % y 	
# ** 	        Exponentiation 	        x ** y 	
# // 	        Floor division 	        x // y


x=12
y=5

#-------------------------Addition------------
ans=x+y
mystr="Sum of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Sum of 12 and 5 is : 17

#-------------------------Subtraction------------
ans=x-y
mystr="Subtraction of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Subtraction of 12 and 5 is : 7

#-------------------------Multiplication------------
ans=x*y
mystr="Multiplication of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Multiplication of 12 and 5 is : 60

#-------------------------Division------------
ans=x/y
mystr="Division of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Division of 12 and 5 is : 2.4

#-------------------------Modulus------------
ans=x%y
mystr="Modulus of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Modulus of 12 and 5 is : 2

#-------------------------Exponentiation------------
x=5
y=2
ans=x**y
mystr="Exponentiation of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Exponentiation of 5 and 2 is : 25

#-------------------------Floor division------------
x=20
y=3
ans=x//y
mystr="Floor division of {} and {} is : {}"
print(mystr.format(x, y, ans))
#Floor division of 20 and 3 is : 6

#---------------------------End of Arithmetic Operators---------------------


#---------------------------Python Assignment Operators---------------------

        # Operator 	Example 	Same As 	
        # = 	        x = 5 	    x = 5 	
        # += 	        x += 3 	    x = x + 3 	
        # -= 	        x -= 3 	    x = x - 3 	
        # *= 	        x *= 3 	    x = x * 3 	
        # /= 	        x /= 3 	    x = x / 3 	
        # %= 	        x %= 3 	    x = x % 3 	
        # //= 	    x //= 3 	x = x // 3 	
        # **= 	    x **= 3 	x = x ** 3 	
        # &= 	        x &= 3 	    x = x & 3 	
        # |= 	        x |= 3 	    x = x | 3 	
        # ^= 	        x ^= 3 	    x = x ^ 3 	
        # >>= 	    x >>= 3 	x = x >> 3 	
        # <<= 	    x <<= 3 	x = x << 3



#-------------------------=------------
my_var=10
print(my_var)
#10

#-------------------------+=------------
my_var+=10
print(my_var)
#20

#--------------------------=------------
my_var-=2
print(my_var)
#18

#-------------------------*=------------
my_var*=2
print(my_var)
#36

#-------------------------/=------------
my_var/=4
print(my_var)
#9.0

#-------------------------%=------------
my_var%=5
print(my_var)
#4.0

#-------------------------**=------------
my_var**=5
print(my_var)
#1024.0


#---------------------------End of Python Assignment Operators---------------------


#---------------------------Python Comparison Operators---------------------


# Operator 	        Name 	                        Example 
# == 	                Equal 	                        x == y 	
# != 	                Not equal 	                    x != y 	
# > 	                Greater than 	                x > y 	
# < 	                Less than 	                    x < y 	
# >= 	                Greater than or equal to 	    x >= y 	
# <= 	                Less than or equal to 	        x <= y


#-------------------------=------------
x=5
y=10
#--------------------- == -------------------------------
if x==y:
    print("Value of x and y are equal.")
else:    
    print("== Condition failed")
#

#--------------------- != -------------------------------
if x!=y:
     print("Value of x and y are not equal.")
else:    
    print("!= Condition failed")

#--------------------- > -------------------------------
if x>y:
     print("Value of x is greater than y.")
else:    
    print("> Condition failed")


#--------------------- < -------------------------------
if x<y:
     print("Value of x is less than y")
else:    
    print("< Condition failed")

#--------------------- >= -------------------------------
if x>=y:
     print("Value of x is greater than or equal to y")
else:    
    print(">=Condition failed")

#--------------------- <= -------------------------------
if x<=y:
     print("Value of x is less than or equal to y")
else:    
    print("<= Condition failed")


#---------------------------End of Python Comparison Operators---------------------


#  5 (Five) Functions
print('Assignment -1')

def my_fun():
    print ('I am in function')
   
my_fun()  

#---------------------------------------------
print('Assignment -2')

def fun_add(a,b):
    return a+b
x=int(input('Please enter the value of x : '))
y=int(input('Please enter the value of y : '))
print ('Sum of ' + str(x) + ' and ' + str(y) + ' : ' + str(fun_add(x,y)) )

#---------------------------------------------
print('Assignment -3')
def my_sq(a):
    return a*a

print(my_sq(3))

#---------------------------------------------
print('Assignment -4')
def my_sq(a):
    return a*a

for i in range(1,10,1):
    result=my_sq(i)
    print(result)

#---------------------------------------------

def fun_recursion(i):
    if(i > 0):
        r=i+fun_recursion(i-1)
        print(r)
    else:
        r = 0
    return r
fun_recursion(6)   
#---------------------------------------------



def sum_total(*ar):
    sum=0
    for i in ar:
        sum=sum+int(i)
    return sum

print(sum_total(4,6,7,8,4))  
#---------------------------------------------


def my_name(**name):
    print("Har first name is : " + name["f_name"])
    print("Har last name is : " + name["l_name"])

my_name(f_name = "Shaira", l_name = "Tahsin")
    
#---------------------------------------------


def my_add(**arg):
    s = 0
    for i in arg:
        s = s + arg[i]
    return s

total = my_add(a=54,b=67,c=23,d=46,e=10,f=50)
print('Sum is : ',total)

#----------------------Calculator using Function-----------------------


def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def multiplication(a,b):
    return a*b  

def division(a,b):
    if b!=0:
        return a/b
    else:
        return 0
    
x=int(input("Enter a value for x : "))
y=int(input("Enter a value for y : "))

z=input("Options are (+-*/ or x for exit) : ")
while (z!=0):
  if (z=='+'):
    print(add(x,y))
    
  elif(z=='-'):
    print(sub(x,y))
  
  elif(z=='*'):
    print(multiplication(x,y))
  
  elif(z=='/'):
    print(division(x,y))
  
  elif (z=='x'):
    exit()
  z=input("Options are (+-*/ or x for exit) : ")



#----------------------------------------------------------------------------



class MyCal:
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def multiplication(self,a,b):
        return a*b

    def division(self,a,b):
        return a/b



   
x=int(input("Enter a value for x : "))
y=int(input("Enter a value for y : "))

Calc1=MyCal()

print (Calc1.add(x,y))
print (Calc1.sub(x,y))
print (Calc1.multiplication(x,y))
print (Calc1.division(x,y))


#------------------------------------------------

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#------------------------------------------------


class MyClass:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def multiplication(self):
        return self.a*self.b

    def division(self):
        return self.a/self.b

 
x=int(input("Enter a value for x : "))
y=int(input("Enter a value for y : "))

Calc1=MyClass(x,y)

print (Calc1.add())
print (Calc1.sub())
print (Calc1.multiplication())
print (Calc1.division())





#------------------------------------------------

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname() 
#------------------------------------------------

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 

#------------------List------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#-----------Tuples------------------------
mytuple = ("apple", "banana", "cherry")
print(mytuple)

#-----------Tuples------------------------

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)



fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)



thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


thisset = {"apple", "banana", "cherry"}
print(len(thisset)) 



thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)



thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 

#----------------Function--------------------

def my_function():
  print("Hello from a function")
my_function()



#----------------Class--------------------
class FirstClass:
    a=4
    b=6
student1=FirstClass()
print(student1.a,student1.b)

# #-------------------------------------------

class EmpName:
    f_name='Md.'
    l_name='Hasanuzzaman'
emp=EmpName()
print(emp.f_name,emp.l_name)

class Emp_detail:
    id = 19990006
    Name = "Aslam"
    Age = 50
    
emp=Emp_detail()

print(emp.id,emp.Name,emp.Age)

#------------------------------------------------
class Calc:
    def add(self,num1,num2):
        return num1+num2

my_calc=Calc()  
print (my_calc.add(3,6))

#------------------------------------------------

class Cal:
    def add(self):
        return 4+5
cal=Cal()
print(cal.add())



#---------------------------Inheritance------------------------------
class Person:
    def Information(self,id,name,designation):
        return id,name,designation

class Student(Person):
    def Information(self,std_roll,sub):
        return std_roll,sub

em_obj=Student()
my_var=em_obj.Information(2,'Hasan')
my_var1=em_obj.std_info('20091220','Math')
print (my_var,my_var1)



#---------------------------Decorator------------------------------
def d_fun(fun):
    def wrapper():
        int('###')
        fun()
        fun()
        fun()
        print ('@@@')
    return wrapper
@d_fun
def a_dec():
    return 'Hello'
print('Hello')

        


'''