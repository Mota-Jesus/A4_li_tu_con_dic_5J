print("Ejemplos de tuplas")
canciones=("Parte De","PABLO","LINDO")
print(canciones)
y = list(canciones)
print(y)
y[1] = "Fascination"
x = tuple(y)
print(x)

print("Listado de elementos de la tupla canciones ciclo for")
for Mota in canciones:
    print(Mota)
