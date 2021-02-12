def dup(arry):
    arr_position = 0
    posicion_letra
    for word in arry:
        lista = []
        position_in_word = 0
        arr_position += 1
        num_letras = word.count()
        while num_letras > position_in_word:
            letter = word[position_in_word]
            letter_dos = word[position_in_word+1]
            if letter == letter_dos:
                
                



            position_in_word += 1

            
            if rest == 1 or rest== -1:
                resultado = word[:first_letter] + word[first_letter+1:]
                lista.append(resultado)
    return lista


if __name__ == "__main__":
    assert (dup(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]),['codewars','picaniny','hubububo'])




                

            