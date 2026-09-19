def next_permutation(nums):
    n = len(nums)

    # Find the first decreasing element from the right
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Find the next larger element and swap
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the suffix in-place
    left = i + 1
    right = n - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


# Test
print(next_permutation([1, 2, 3])) # [1, 3, 2]
print(next_permutation([3, 2, 1])) # [1, 2, 3]