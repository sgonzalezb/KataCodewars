def find_outlier(integers):
    impar = []
    par = []
    for num in integers:
        if num % 2 == 0:
            par.append(num)
        elif num % 2 != 0:
            impar.append(num)
    if len(par) > len(impar):
        return impar[0]
    else:
        return par[0]

if __name__ == "__main__":
    assert (find_outlier([2, 4, 6, 8, 10, 3]), 3)
    assert (find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
    assert (find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)