def get_consective_items(items, key):
    items = str(items)
    key = str(key)
    contador = 0
    for i in items:
        if i == key:
            contador += 1
    return contador
            

if __name__ == "__main__":
    assert get_consective_items(90000, 0) == 4
    assert get_consective_items('ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii', 'i') == 11