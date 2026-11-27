from utils import normalize

# def merge(nums: list[int], left: int, right: int, mid: int):
#     left_copy = nums[left:mid + 1]
#     right_copy = nums[mid + 1: right]
#     l_counter, r_counter = 0, 0
#     sorted_counter = left

# def merge_sort(nums: list[int]) -> list[int]:

#     # base case
#     if left >= right:
#         return nums
    
#     mid = len(arr) // 2
#     # want to ignore mid value here
#     merge_sort(nums, left, mid)  # left side
#     merge_sort(nums, mid + 1, right)

#     merge(nums, left, right, mid)


def three_sum(nums: list[int]) -> list[list[int]]:
    if not nums:
        return nums

    master_list = []
    nums.sort()
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break  # bc list is sorted, all future totals will be > 0
        elif i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                master_list.append([nums[i], nums[j], nums[k]])
                k -= 1
                j += 1

                # increment j to skip duplicates
                # NOTE: don't need to decrement k bc,
                #   the guaranteed-larger-value at index j will always have the total > 0,
                #   and k will automatically decrement until the total < 0 || total == 0 || j >= k
                while j < k and nums[j] == nums[j - 1]:
                    j += 1

    return master_list
        

if __name__ == "__main__":
    test = [-1,0,1,2,-1,-4]
    expected = [[-1,-1,2],[-1,0,1]]

    result = three_sum(test)
    if normalize(result) == normalize(expected):
        print("All test cases passed.")
