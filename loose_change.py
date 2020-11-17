
def loose_change(input):
    nombre_monedas = ["Pennies","Nickels","Dimes","Quarters"]
    valor_monedas = [1, 5, 10, 25]
    dicc_monedas = dict(zip(nombre_monedas,valor_monedas))
    monedas = 0 
    lista_vacia = []
    change_dict = dict(zip(nombre_monedas.reverse,lista_vacia))
    valor_monedas = valor_monedas.reverse()
    for item in valor_monedas:
        while input > item:
            input -= item
            monedas += 1
            lista_vacia.append(monedas)
    return change_dict
     
        

        

            
            
                 
if __name__ == "__main__":  
    assert loose_change(29),  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}






        #if input > item:
         #   input -= item
        #else continue
        

