def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return []  # If no solution is found

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print("Two Sum result:", two_sum(nums, target))



def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return []  # Should never happen as there is exactly one solution in the contest constraints

# Example
nums = [2, 7, 11, 15]
target = 9
print("Two Sum result:", two_sum(nums, target))
