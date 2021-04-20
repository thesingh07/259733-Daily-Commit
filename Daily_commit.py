#Solo learn project practice
# 1.Exponentiation
print(0.01*2**30)

# 2.Simple calculator
a=int(input())
b=int(input())
print(a+b)

# 3.FizzBuzz
n = int(input())
for x in range(1, n, 2):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
        continue
    elif x % 3 == 0:
        print("Solo")
        continue
    elif x % 5 == 0:
        print("Learn")
        continue
    else:
        print(x)
		
# 4.Celsius to Fahrenheit
celsius = int(input())
def conv(c):
    return (c*9/5)+32
fahrenheit = conv(celsius)
print(fahrenheit)

# 5.Book Titles
file = open("/usercode/files/books.txt", "r")
for line in file:
    title=line.replace('\n',"")
    count=len(title)
    print(f'{title[0]}{count}')
file.close()

# 6.Longest Word
txt=input().split()
print(max(txt,key=len))

# 7.Fibonacci
num = int(input())
def fibonacci(n):
  if n<=1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(num):
 print(fibonacci(i))
 
# 8.Juice Maker
class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

    def __add__(self,other):
        new_name = self.name + "&" + other.name
        new_capacity= self.capacity + other.capacity
        return Juice(new_name,new_capacity)

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)

# 9.Phone Number Validator
import re
num = str(input())
pattern="\A(1|8|9)\d{7}$"
if re.match(pattern,num):
    print("Valid")
else:
    print("Invalid") 
	
# 10.Adding Words
def concatenate(*args):
   return '-'.join(args)
print(concatenate("I", "love", "Python", "!"))