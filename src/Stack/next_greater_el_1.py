def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = []
    result = {}

    # start at last and end at first inclusive
    for i in range(len(nums2) - 1, -1, -1):
        current = nums2[i]
        # pop elements <= current; stop when stack is empty or top > current
        while stack and stack[-1] <= current:
            stack.pop()

        if stack:  # if theres still elements, then theres a NGE for 'current'
            result[current] = stack[-1]
        else:      # if theres no more elements, then theres NO NGE for 'current'
            result[current] = -1

        stack.append(current)

    return [result[num] for num in nums1]

if __name__ == "__main__":
    test_nums1 = [4,1,2]
    test_nums2 = [1,3,4,2]
    expected = [-1, 3, -1]

    result = next_greater_element(test_nums1, test_nums2)
    print("PASSED.") if result == expected else print("FAILED.")
