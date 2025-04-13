def prime():
    # This function checks if the number entered by the user is a prime number
    num = int(input("Enter a number: "))
    
    if num < 2:
        print("The number is not prime")
        return
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("The number is not prime")
            return
    
    print("The number is prime")