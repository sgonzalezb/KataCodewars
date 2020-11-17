

def array_plus_array(arr1,arr2):
    suma_1 = 0
    for item in arr1:
        suma_1 += item
    suma_2 = 0
    for item in arr2:
        suma_2 += item
    suma = suma_1 + suma_2
    return suma



if __name__ == "__main__":
    print("Basic tests")
    assert array_plus_array([1,2,3],[1,2,3]) == 12