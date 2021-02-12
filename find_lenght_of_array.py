def length_of_sequence(arr,n):
    if arr.count(n) == 2:
        primer = arr.index(n,0)
        segundo = arr.index(n,primer+1)
        lista = arr[primer:segundo+1]
        contador = 0
        for item in lista:
            contador += 1
        return contador
    else:
        return 0