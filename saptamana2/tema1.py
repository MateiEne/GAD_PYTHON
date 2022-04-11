lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
lista_desc = lista[0:]
lista_asc = lista[0:]

lista_desc.sort(reverse=True)
lista_asc.sort();

print(lista_desc)
print(lista_asc)
print(lista)

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(l[::2])
print(l[1::2])

for i in lista:
    if i % 3 == 0:
        print(i)

