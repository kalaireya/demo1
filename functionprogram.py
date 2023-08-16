# sum of two num
def sum(num1,num2):
    res=num1+num2
    print(res)
    return"wow"    
print("sum of two num")
w=sum(89,11)
print(w)
# input as a string an return the length of string
def string(input):
 return(len(input))
print("length of string")
s=string("kalai")
e=string("reya")
print(s,"\n",e)
# Write a function that takes a list of integers as input
#  and returns the sum of all the even numbers in the list.
def even(num):
    sum1=0
    for list in num:
      if list%2==0:
        sum1+=list
    return sum1
print("sum of even num")
even_num=[1,8,7,9,4,6,21,22,25,26,38,45,]
print(even(even_num))
# Write a function that takes a 
# list of strings as input and returns the longest string in the list.
def strg(longs):
    kstr=""
    for lstr in longs:
        if len(lstr)>len(kstr):
            kstr=lstr
    return(kstr)
print("longest of given string")
longs=["kalai","king","chairsandbed","pairs","sodamp"]
print(strg(longs))
            


