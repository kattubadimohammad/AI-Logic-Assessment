def length_of_longest_substring(s):
    seen = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


# Test
print(length_of_longest_substring("abcabcbb")) # 3
print(length_of_longest_substring("bbbbb"))    # 1