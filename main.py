# https://repl.it/talk/learn/Learn-To-Code-In-Python/7484

print('Hello world!')

# Write some comments!

'''
Dear PYer,
I am confused about how you said you could use triple quotes to make
SUPER
LONG
COMMENTS
!

I am wondering if this is true,
and if so, 
I am wondering if this is correct.

Could you help me with this?

Thanks,
Random guy who used your tutorial.
'''
print('Testing')

x = 5
y = 7
z = x*y # 35
print(z) # => 35

x = 5
x = str(x)
b = '5'
b = int(b)
print('x = ', x, '; b = ', str(b), ';') # => x = 5; b = 5;
print('x = '+ x+ '; b = '+ str(b)+ ';') # => x = 5; b = 5;

x = 4
a = x + 1; print(a)
a = x - 1; print(a)
a = x * 2; print(a)
a = x / 2; print(a)

a += 1; print(a)
a -= 1; print(a)
a *= 2; print(a)
a /= 2; print(a)

x = 'hello'; print(x) # Good
x = "hello"; print(x) # Good
# x = "hello' # ERRORRR!!!

x = 'Hello everybody!'
y = x[1]; print(y) # 'e'
y = x[-1]; print(y) # '!'
y = x[5]; print(y) # ' '
y = x[1:]; print(y) # 'ello everybody!'
y = x[:-1]; print(y) # 'Hello everybod'
y = x[2:-3]; print(y) # 'llo everyb'

x = " Testing, testing, testing, testing       "
print(x.strip())
print(len(x))
print(x.lower())
print(x.upper())
print(x.replace('test', 'runn'))
print(x.split(','))

print('Type something: ')
x = input()
print('Here is what you said: ', x)

print('Here is what you said: ', input('Type something: '))

import random
print(random.randint(3,5)) # Prints a random number between 3 and 5

from time import sleep
for i in range(100):
     print('Hello', str(i))
     sleep(.3)

import time
for number in range(100):
     print(number)
     time.sleep(.1)

#while True: # Runs forever
#     print('Hello World!')

import random
position = '<placeholder>'
while position != 1: # will run at least once
    position = random.randint(1, 10)
    print(position)

