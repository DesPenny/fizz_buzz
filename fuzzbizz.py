import sys

if len(sys.argv) == 1:
  my_input = raw_input("Dude, enter a number yo: ")
   
else:
  my_input = sys.argv[1]
  
str(my_input)
try:
  n = int(my_input)
except:
    my_input = raw_input("Sorry Dude you didn't enter a valid integer. Try again: ")
    n = int(my_input)
for n in range(1,n+1):
  if n % 3 ==0 and n%5==0:
    print 'FizzBuzz'
  elif n%3==0:
    print 'Fizz'
  elif n%5==0:
    print 'Buzz'
  else:
    print (n)