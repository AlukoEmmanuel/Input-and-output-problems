# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b

# # Example
# n = 10
# print(f"Fibonacci F({n}) =", fibonacci(n))
# # Compare this snippet from Two%20Sum.py:
# def fibonacci(n):# This function calculates the nth Fibonacci number using an iterative approach
#      # what is an iterative approach? an iterative approach is a method of solving a problem
#      # by repeatedly applying a set of instructions until a desired result is achieved.
#      # In this case, we are repeatedly calculating the Fibonacci numbers until we reach the nth number.
#    if n <= 0:# Check for invalid input
#        return 0 # Base case explain? base case is a condition that stops the recursion or iteration in a function.
#     # In this case, if n is less than or equal to 0, we return 0.
#    elif n ==1:
#        return 1 # Base cases for Fibonacci numbers
#    # The first Fibonacci number is 1.
#     # The second Fibonacci number is also 1.
#     # The third Fibonacci number is 2. The fourth Fibonacci number is 3.
#    a, b = 0,1 # Initialize the first two Fibonacci numbers
#    for _ in range(2, n+1):# Iterate from 2 to n let me explain more about this line the 
# # for _ in range(2, n+1): means that we are iterating from 2 to n inclusive.
#          a, b = b, a + b # Update the Fibonacci numbers explain this line
# # In this line, we are updating the values of a and b.
# # The new value of a becomes the old value of b, and the new value of b becomes the sum of the old values of a and b.
# # This is how we calculate the Fibonacci numbers iteratively.
# # The first iteration will give us the second Fibonacci number.
# # The second iteration will give us the third Fibonacci number.
#          return b # Return the nth Fibonacci number

# n = int(input("Enter a number: ")) # Get user input
# print(f"The {n}th Fibonacci number is: {fibonacci(n)}") # Print the result

def fibonacci(s):
    if s<=0:
        return 0
    elif s==1:
        return 1
    a,b=0,1
    for _ in range(2,s+1):
        a,b=b,a+b
    return b
# Example usage
s = int(input("Enter a number: "))
print(f"The {s}th Fibonacci number is: {fibonacci(s)}")