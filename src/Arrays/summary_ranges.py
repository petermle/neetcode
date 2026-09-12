from utils import normalize

def summaryRanges(nums: list[int]) -> list[str]:
    if not nums:
         return []
    
    i = 0
    result = []
    
    while i < len(nums):
        start = nums[i]
        while i < len(nums) - 1 and (nums[i] + 1) == nums[i + 1]:  # consecutive
            i += 1

        if start == nums[i]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[i]}")

        i += 1

    if i <= len(nums) - 1 and nums[i] - 1 != nums[i - 1]:
        result.append(str(nums[i]))

    return result
             

if __name__ == "__main__":
    test_1 = [0, 1, 2, 4, 5, 7]
    test_2 = [0, 2, 3, 4, 6, 8, 9]
    test_1_expected = ["0->2","4->5","7"]
    test_2_expected = ["0","2->4","6","8->9"]

    print(summaryRanges(test_1))
    if summaryRanges(test_1) == test_1_expected:
        print("Test case 1 passed.")
    else:
        print("Test case 1 failed.")

    if summaryRanges(test_2) == test_2_expected:
        print("Test case 2 passed.")
    else:
        print("Test case 2 failed.")
