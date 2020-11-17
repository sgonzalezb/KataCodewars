def factorial(num):
    # 3! (fatorial de 3) = 3 * 2 * 1
    #para hacer un sumatiorio o un productorio hay que hacer unos acumuladores (suma = 0 , productorio = 1)
    # 1 * 2 * 3 .... * numero
    productorio = 1 #ACUMULADOR
    entero = 1
    while entero <= num : #SI ESCRIBIMOS UN BUCLE DEBEMOS ESCRIBIR UNA MODIFICACIÓN DEL PROPIO BUCLE (ENTERO)
       productorio = entero * productorio 
       entero = entero + 1
    return productorio
         

if __name__ == "__main__":
    assert factorial(0) == 0
    assert factorial(1) == 1
    assert factorial(3) == 6