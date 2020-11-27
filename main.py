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
z = x * y  # 35
print(z)  # => 35

x = 5
x = str(x)
b = '5'
b = int(b)
print('x = ', x, '; b = ', str(b), ';')  # => x = 5; b = 5;
print('x = ' + x + '; b = ' + str(b) + ';')  # => x = 5; b = 5;

x = 4
a = x + 1
print(a)
a = x - 1
print(a)
a = x * 2
print(a)
a = x / 2
print(a)

a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)

x = 'hello'
print(x)  # Good
x = "hello"
print(x)  # Good
# x = "hello' # ERRORRR!!!

x = 'Hello everybody!'
y = x[1]
print(y)  # 'e'
y = x[-1]
print(y)  # '!'
y = x[5]
print(y)  # ' '
y = x[1:]
print(y)  # 'ello everybody!'
y = x[:-1]
print(y)  # 'Hello everybod'
y = x[2:-3]
print(y)  # 'llo everyb'

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
print(random.randint(3, 5))  # Prints a random number between 3 and 5

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
while position != 1:  # will run at least once
    position = random.randint(1, 10)
    print(position)

import random
num = random.randint(1, 10)
if num == 3:
    print('num is 3. Hooray!!!')
    print(num)
if num > 5:
    print('Num is greater than 5')
    print(num)
if num == 12:
    print(
        'Num is 12, which means that there is a problem with the python language, see if you can figure it out. Extra credit if you can figure it out!'
    )
    print(num)

import random
num = random.randint(1, 10)
if num == 3:
    print('Num is three, this is the only msg you will see.')
    print(num)
elif num > 2:
    print('Num is not three, but is greater than 1')
    print(num)

import random
print(random.randint(1, 9))
print('Wow that was interesting.')
print(random.randint(1, 9))
print('Look at the number above ^')
print(random.randint(1, 9))
print('All of these have been interesting numbers.')
print(random.randint(1, 9))
print("these random.randint's are getting annoying to type")
print(random.randint(1, 9))
print('Hi')
print(random.randint(1, 9))
print('j')

import random


def r(t):
    print(random.randint(1, 9))
    print(t)


r('Wow that was interesting.')
r('Look at the number above ^')
r('All of these have been interesting numbers.')
r("these random.randint's are getting annoying to type")
r('Hi')
r('j')
