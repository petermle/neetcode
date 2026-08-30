def products_of_array_except_self(nums):
    """
    :param nums: integer array
    :return: a list of integers where output[i] is the product
        of all elements of nums except num[i]
    :example: [1,2,4,6] -> [48,24,12,8]
    """
    output = []
    length = len(nums)
    for i in range(length):
        # break into 2 lists (left and right)
        two_lists = nums[0:i] + nums[i + 1:length]

        # map all items in two_list to string equivalents,
        # join items with '*' as delimiter
        # evaluate new string that should look like: "1*2*4*6"
        product = eval("*".join((map(str, two_lists))))
        output.append(product)

    return output

if __name__ == '__main__':
    test_case_1 = [1, 2, 4, 6]
    result = products_of_array_except_self(test_case_1)
    print(f"{result = }")
