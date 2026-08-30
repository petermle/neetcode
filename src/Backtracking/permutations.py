def permute(nums: list[int]) -> list[list[int]]:
    """
    main idea:
        loop through 'nums' with range(),
        remove nums[i] and recurse with sublist,
        repeat/recurse until 1 element in nums -> then return nums as list[list[int]],
        enter inner for loop and iterate through all new permutations created (may be more than 1),
        add the previously removed element to each permutation in new permutations 
        (each original p. in new_p. is guaranteed to not have the previously removed element -> append it),
        after taking each permutation and appending the previously removed element -> append to something like a 'master' list,
        restore nums at the end of each outer loop iteration to maintain outer loop range functionality,
        return as a 'master' list of the new permutations and send it up
    """

    # base case
    if len(nums) <= 1:
        return [nums]

    return_list = []
    for i in range(len(nums)):
        removed = nums.pop(i)

        new_permutations = permute(nums.copy())  # recurse w/ copy to prevent modifying original 'nums'
        for permutation in new_permutations:
            permutation.append(removed)
            return_list.append(permutation)

        nums.insert(i, removed)  # restore nums to maintain outer for loop's number of iterations

    return return_list

if __name__ == "__main__":
    test_case = [1,2,3]
    output = permute(test_case)
    print(f"output: {output}")