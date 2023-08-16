# funtion used for repitation
# builtin function like range,int,input
for i in range(1,10):
    print(i,end=" ")
# user defined function
# must have def function name ():
#passing a parameter without using keyword
def food(name,price):
 return print(name,"it was so delicious")
 return print("Rate",price,"\n have a fun day")
print("\nwelcome to food review")
food("momos",250)
# using keyword
print(" welcome to reya resturant")
food(name="biryani",price="150")
# without using parameter value
def message():
 print("we love India")
#  call function
print("freedom")
message()
# it will show error for one arg
print("how we define one argument in food review")
food("chicken",150)