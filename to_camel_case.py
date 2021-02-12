def to_camel_case(text):
    if text.find("_") != -1:
        barra = text.find("_")
    else:
        barra = text.find("-")
    while barra != -1:
        letra = text[barra+1]
        letra = letra.upper()
        text = text[:barra] + letra + text[barra+2:]
        if text.find("_") != -1:
            barra = text.find("_")
        else:
            barra = text.find("-")       
    return text           