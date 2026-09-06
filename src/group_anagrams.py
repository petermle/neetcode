# utility for normalizing lists for comparison of contents, rather than order
def normalize(groups):
    return sorted([sorted(group) for group in groups])

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    main idea: 
    0. create a 'frequency_dict' that represents char_frequency: words with char_frequency
    1. go through each str in strs
        i. make a new list for each str
        ii. create an array representation off character frequency
        iii. check in 'frequency_dict' if 'new_list' is already present
            a. if it is, then append the word to the key's value (which is a list of strs)
            b. if it is NOT, then create a new entry in the dict. and create a list with the current word in it
    2. loop through the dict and add all the lists into one 'master list' (which is the result)
    3. return master list
    """

    result = []
    frequency_dict: dict[list[int], list[str]] = {}

    for str in strs:
        new_list = [0] * 26  # 26 letters in alphabet
        for char in str:
            index = ord(char.lower()) - 97  # offsetting
            new_list[index] += 1

        new_list = tuple(new_list)  # cast to tuple so we can insert into 'frequency_dict'
        if new_list in frequency_dict:
            frequency_dict[new_list].append(str)
        else:
            frequency_dict[new_list] = [str]
        """
        could also be: frequency_dict.setdefault(new_list, []).append(str)
        saying: does this new_list exist in frequency_dict?
            if yes, simply append str to frequency_dict's value at that key
            if no, create a list as the value at that key, then append str to it
        NOTE: .setdefault() method returns a reference to the value at that key,
                so that's why you can method chain with .append()
        """

    for value in frequency_dict.values():
        result.append(value)

    return result
    
    
if __name__ == "__main__":
    test_cases = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ['a']
    ]
    expected = [
        [["bat"],["nat","tan"],["ate","eat","tea"]],
        [[""]],
        [['a']]
    ]

    for i in range(len(test_cases)):
        result = group_anagrams(test_cases[i])
        if normalize(result) != normalize(expected[i]):
            print(f"Test Case: {test_cases[i]} failed.")
            print(f"\tExpected: {expected[i]}")
            print(f"\tActual Type: {result}")
            break
    else:
        print("All test cases passed.")
