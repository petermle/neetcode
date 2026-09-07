def isValid(s: str) -> bool:
    if len(s) < 2:
        return False

    stack = []
    opening = {'(', '{', '['}
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for ch in s:
        if ch in opening:
            stack.append(ch)
        elif ch in pairs:
            if not stack:
                return False
            
            bracket = stack.pop()
            matching_bracket = pairs[ch]
            if bracket != matching_bracket:
                return False
        else:
            return False

    return len(stack) == 0

if __name__ == "__main__":
    test = "(){}[]"
    result = isValid(test)
    print(result)
