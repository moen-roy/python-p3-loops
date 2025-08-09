#!/usr/bin/env python3

def happy_new_year():
    i= 10
    while i> 0:
        print(i)
        i-=1
        print("Happy New Year!")
    # code goes here!
    pass

def square_integers(int_list):
    # list comprehensions
    return [x**2 for x in int_list]
    print (int_list)
    # code goes here!
    pass

def fizzbuzz():
    for num in range(1, 101):  # From 1 to 100 inclusive
        if num % 15 == 0:      # Check divisible by both 3 and 5 first
            print("FizzBuzz")
        elif num % 3 == 0:     # Then check divisible by 3
            print("Fizz")
        elif num % 5 == 0:     # Then check divisible by 5
            print("Buzz")
        else:
            print(num)         # Print the number if none apply
    
    pass





# i = 0
# while i < 905:
#     print(f"Count: {i}")
#     i += 100 # Equivalent to i++ in JavaScript
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruits[0])
# evens = [x for x in range(20) if x  == 0]
# print(evens)