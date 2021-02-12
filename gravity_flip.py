def flip(d, a):
    if d == "R":
        mayor = sorted(a)
        return mayor
    if d == "L":
        menor = sorted(a,reverse=True)
        return menor
if __name__ == "__main__":
    assert flip('R', [3, 2, 1, 2])==([1, 2, 2, 3])
    assert flip('L', [1, 4, 5, 3, 5]) == ([5, 5, 4, 3, 1])
