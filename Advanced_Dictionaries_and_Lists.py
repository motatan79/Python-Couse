d = {'k1': 1, 'k2': 2}

a = {x:x**2 for x in range(10)}
print(a)

# ------------- LISTS -----------

l = [1, 2, 3]
print(l)
l.append(4)
print(l)

print(l.count(10))

# Se usa extend para añadir muchos elementos a la lista
x = [1, 2, 3]
x.extend([4,5])
print(x)

print(l.index(2))

# Insert pasando el index
x.insert(2,'inserted')
print(x)

# Remove remueve la primera aparición del elemento
x.remove('inserted')
print(x)

# Reverse , voltea la lista existente
x.reverse()
print(x)

# Sort, ordena los elementos
x.sort()
print(x)
