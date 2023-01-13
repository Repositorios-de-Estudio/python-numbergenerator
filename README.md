# NUMBER GENERATOR

Un teclado de solo dígitos contiene 10 dígitos del 0 al 9. Todos existen en una línea.

Dada una cadena de 10 que ilustra cómo se colocan las teclas. Para escribir un dígito, comience desde el índice 'cero' hasta el índice del dígito de destino. Tomó abs(a-b) ms pasar del índice 'a' al índice 'b'.

Escribe una función para calcular el número de ms necesarios para escribir con un dedo.

## Ejemplo 1:

### Entrada: 
`"0123456789"`
`"210"`

### Salida:
`4`

## Ejemplo 2:

### Entrada:
`"8459761203"`
`"5439"`

### Salida:
`17`

## Estrategia Solución

La estrategia es llegar a calcular la distancia entre los valores de num con respecto a digits. 

`distancia = ABS(indiceA - indiceB)`

* indiceA es el indice que se va desplazando por num en busqueda del valor num[indice], indiceB es el indice que corresponde al valor num[indice] en la cadena digitis.
