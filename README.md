# Competiton preparation HPE Codewars 2025
## Coding Problems in Repository

This repository contains a collection of coding problems with concise problem descriptions, key techniques, and sample Python solutions. These examples cover a broad range of topics that are commonly encountered in coding competitions like HPE CodeWars.

---

## Table of Contents

1. [Magic Door Problem](#magic-door-problem)
2. [Two Sum](#two-sum)
3. [Reverse a String](#reverse-a-string)
4. [Fibonacci Sequence](#fibonacci-sequence)
5. [Valid Parentheses](#valid-parentheses)
6. [Rotate Array](#rotate-array)
7. [Merge Intervals](#merge-intervals)
8. [Longest Substring Without Repeating Characters](#longest-substring-without-repeating-characters)
9. [Find Peak Element](#find-peak-element)
10. [Search in a Rotated Sorted Array](#search-in-a-rotated-sorted-array)
11. [Coin Change Problem](#coin-change-problem)

---

## Magic Door Problem

**Description:**  
Determine if the "magic door" opens based on an input number.

- **If the number is even:** Print `"Door opens"`.
- **If the number is odd and divisible by 5:** Print `"Door opens with a spell"`.
- **Otherwise:** Print `"Door remains closed"`.

**Sample Code:**
```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Door opens")
elif number % 2 != 0 and number % 5 == 0:
    print("Door opens with a spell")
else:
    print("Door remains closed")
