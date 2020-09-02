

#recursive approach to find factorial.
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num*factorial(num-1))

number  = int(input("Enter a number for factorial.\t"))

print(factorial(number))

   


