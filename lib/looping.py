#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while(num >= 1):
        print(num)
        num -= 1
        if num == 0:
            print("Happy New Year!")

def square_integers(int_list):
    square_list = [int**2 for int in int_list]
    return square_list

def fizzbuzz():
   for i in range(1,101):
    if i % 3 == 0 and i%5 == 0:
       print(f"FizzBuzz")
    elif i % 3 == 0 :
       print(f"Fizz")
    elif i % 5 == 0 :
       print(f"Buzz")
    else:
       print(i)

print(happy_new_year())
print(square_integers([1,2,3,4,5]))
print(fizzbuzz)