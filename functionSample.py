def hey():
    print("hey")

hey()

#passing values to a function

def hey(value,age):
    print("My name is "+value + " , age : " +str(age))

age = 20
hey("Chandhu",age)

#to pass a number of arguments to a function

def hello(*values) :
    print("First : " + values[0] + " second : " + values[1])

hello("hello","hey","one")

#concept of local and global variable

value = 10
def val():
    value = 25
    print(value)

print(value) #print global variable
val() #print local variable


#key word argument : can change the orderning of passing arguments
def sample(name,age) :
    print("name : " + name + " age : " + age)

sample(age = "20" , name = "hello")

#default argument
def sample1(name,age = "25") :  # default value of age is 25 
    #that is if the value of age is not passed in function call then default value of age is taken
    print("name : " + name + " age : " + age)

sample1( name = "hello")
sample1( name = "hello", age ="35")


#return 
def add(a,b) :
    sum=a+b
    return sum
res = add (20,30)
print(res)

#dictionary

values = {"name":"hello,hey","place":"Palakkad,TVM" }
print(values)
print(values.get("place"))