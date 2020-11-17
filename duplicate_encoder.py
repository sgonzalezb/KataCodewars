 #si esta repetido: )
 # si NO esta repetido: (
 #
def duplicate_encode(input):
    output = ""
    letra = 0
    input = input.lower()
    for letra in input:
            if input.count(letra) == 1:
                output += "(" 
            else: 
                output += ")"    
    return output
  
















