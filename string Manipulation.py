# def reverse_string(s):
#    return s[::-1]
# if __name__ == "__main__":
#  num = input("Enter a number: ").strip()
#  reversed_string = reverse_string(num)
#  print(f"The reversed string is: {reversed_string}")

# def reverse_string(s):
#    # Option 1: Using slicing
#     return s[::-1]

# # Example usage:
# input_str = input("Enter string:").strip()
# print("Reversed string:", reverse_string(input_str))

# def reverse_string(s):
#     return s[::-1]
# input_str = input("Enter string to revrse:").strip()
# print("Reversed string:", reverse_string(input_str))


def reverse_string(s):
    return s[::-1]
input_string = input("Enter a string to reverse:").strip().lower()
reversed_string = reverse_string(input_string)
print (f"{input_string}, has been reversed to {reversed_string}")