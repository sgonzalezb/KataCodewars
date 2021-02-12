def anagrams(word, words):
    lista_dev = []
    for item in words:
        if sorted(item) == sorted(word):
            lista_dev.append(item)
    return lista_dev
    






if __name__ == "__main__":
    assert anagrams("laser",["lazing","lazy","lacer=="]) == []
    assert anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
    assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']
     