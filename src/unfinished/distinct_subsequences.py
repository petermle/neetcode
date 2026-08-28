def numDistinct(s: str, t: str) -> int:
    # get powerset
    s_set = list(s)
    powerset: list[list] = []
    
    for ch in s_set:
        for s in powerset:
            s_temp = s + [ch]
            powerset.append(s_temp)
        powerset.append([ch])

    print(powerset)

if __name__ == "__main__":
    s = "rabbbit"
    t = "rabbit"
    numDistinct(s, t)
    print(['h'] + ['i'])