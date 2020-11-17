# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.


#OPCIÓN A:  ORDENANDO LA LISTA (NO RECOMENDABLE)
def greatest(list):
    for item in list:
        list.sort()
        if list.count() > 1: 
            return list[-1]
        else:
            return 0


#OPCIÓN B : 

def greatest(list):
    if list == []:
        return 0
    else:
        numb_may = list[0]
        for item in list:
            if item > numb_may:
                numb_may = item
    return numb_may

    




#print greatest([4,23,1])
#>>> 23
#print greatest([])
#>>> 0
