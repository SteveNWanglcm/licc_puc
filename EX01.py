def resumir(texto):
    if len(texto) > 140:
        texto_resumido = str(texto[0,140], replace.texto(texto[141, len(texto)], '(...)'))
    return texto_resumido
