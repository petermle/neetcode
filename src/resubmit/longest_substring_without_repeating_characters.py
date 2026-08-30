def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0

    result = 0
    running = ""
    seen = set()

    for ch in s:
        if ch not in seen:  # new unique character
            seen.add(ch)
            running += ch
        else:
            if len(running) > result:
                result = len(running)
            pivot = running.find(ch)
            for i in range(pivot):
                seen.remove(running[i])  # removing from seen

            running = running[pivot + 1:] + ch

    if len(running) > result:
        result = len(running)
    return result


if __name__ == "__main__":
    test_strings = {
        "abcabcbb": 3,
        "bbbbb": 1,
        "pwwkew": 3,
        " ": 1
    }

    for test in test_strings:
        res = lengthOfLongestSubstring(test)
        if res != test_strings[test]:
            print(f"FAIL: \nexpected: {test} = {test_strings[test]}\nactual: {test} = {res}\n")

