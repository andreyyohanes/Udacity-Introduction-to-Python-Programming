## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

for number in check_prime:
    for factor in range(2, number):
        if number % factor == 0:
            print("{} is not a prime number, because {} is a factor of {}.".format(number, factor, number))
            break
        if factor == number - 1:
            print("{} is a prime number.".format(number))
