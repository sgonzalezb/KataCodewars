def solution(s):
    output = []
    pair = ""
    if len(s) % 2 == 0:
        for letter in s:
            if len(pair) < 2:
                pair += letter
            if len(pair) == 2:
                output.append(pair)
                pair = ""
    else:
        for letter in s:
            if len(pair) < 2:
                pair += letter
            if len(pair) == 2:
                output.append(pair)
                pair = ""
            if len(pair) == 1 and letter == s[-1]:
                pair += "_"
                output.append(pair)
    return output

        
        


if __name__ == "__main__":
    assert solution("asdfads") == ['as', 'df', 'ad', 's_']
    assert solution("asdfadsf") , ['as', 'df', 'ad', 'sf']
        