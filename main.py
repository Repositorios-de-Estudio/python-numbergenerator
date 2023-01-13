
# NUMBER GENERATOR


def solution(digitis: str, num: str) -> int:
    indiceA = 0 # indice presente
    distancia = 0
    indiceB = 0 # indice pasado
    
    #digitis2 = [int(x) for x in digitis]
    
    for item in num:
        indiceB = digitis.index(item)
        distancia += abs(indiceA-indiceB)
        indiceA = indiceB
    return distancia
    
    
if __name__ == '__main__':
    a1 = "0123456789"
    b1 = "210"
    # result = 4

    a2 = "8459761203"
    b2 = "5439"
    # resul = 17

    output = solution(a2, b2)
    print(output)