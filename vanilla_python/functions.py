#declareing a function
#code needs to be indented to be part of the function
def say_hello(name,age):
  print('Hello ' + name + ", you are: " + age )
  



name = input("Enter your name: ")
age = input("Enter your age: ")
#code only gets exicuted by "calling" the function
#use _ when function contains more then one word
say_hello(name, age)




#flow of a program function
# print('Top')
# say_hello()
# print('Bottom')