# def max_subarray_sum(nums):
#     """
#     This function finds the maximum sum of a contiguous subarray using Kadane's Algorithm.
#     :param nums: List[int] - The input array of integers
#     :return: int - The maximum subarray sum
#     """
#     max_current = nums[0]
#     max_global = nums[0]

#     for i in range(1, len(nums)):
#         max_current = max(nums[i], max_current + nums[i])
#         if max_current > max_global:
#             max_global = max_current

#     return max_global

# # Example usage
# if __name__ == "__main__":
#     nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#     print("Maximum Subarray Sum:", max_subarray_sum(nums))  # Output: 6