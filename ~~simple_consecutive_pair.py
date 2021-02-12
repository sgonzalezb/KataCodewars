def pairs(ar):
    lista = []
    pair = ""
    contador = 0
    for item in ar:
        value = item * -1 
        if len(pair) < 2:
            pair += value
        elif pair == 2:
            lista.append(value)
   ¡

    