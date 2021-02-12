def delete_nth(order,max_e):
    list_position = []
    inicio = 0
    for number in order:
        if order.count(number) > max_e:
            posicion = order.index(number,inicio)
            list_position.append(posicion)
            inicio = posicion + 1
        for item in list_position:
            del order[]
    return order







if __name__ == "__main__":
    assert delete_nth([20,37,20,21], 1)==[20,37,21]
    assert delete_nth([1,1,3,3,7,2,2,2,2], 3) == [1, 1, 3, 3, 7, 2, 2, 2]