

#recursive approach to find factorial.
def factorial(num): 
    if num == 1:    # make a base condition so that the function doesn't go to negative indexes.
        return 1
    else:
        return (num*factorial(num-1))   # the same function will be run against the number.

number  = int(input("Enter a number for factorial.\t"))

print(factorial(number))

   


