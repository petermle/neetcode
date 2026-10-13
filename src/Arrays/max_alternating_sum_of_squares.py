def maxAlternatingSum(nums: list[int]) -> int:
    nums = sorted(nums, key=abs)
    length = len(nums)
    total = 0
    
    i = 0
    j = length - 1
    while i < j:
        smallest = nums[i] ** 2
        biggest = nums[j] ** 2
        total += (biggest - smallest)

        i += 1
        j -= 1

    if length % 2 == 1:  # add the middle element if list.len is odd
        total += nums[j] ** 2

    return total

if __name__ == "__main__":
    nums = [1,-1,2,-2,3,-3]
    expected = 16

    if maxAlternatingSum(nums) != expected:
        print("Test failed.")
