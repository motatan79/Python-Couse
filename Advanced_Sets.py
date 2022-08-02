s = set()

s.add(1)

s.add(2)

print(s)

# ELiminar todos los elementos del set
s.clear()

print(s)

# Copiar el set
s = {1,2,3}

sc = s.copy()
print(sc)

s.add(4)

# Para chequear las diferencias entre sets
print(s.difference(sc))

# Para remover todos los elementos coincidentes entre dos sets
s1 = {1,2,3}
s2 = {1,4,5}

s1.difference_update(s2)
print(s1)

# PAra remover un elemento del set
s.discard(2)
print(s)

# Ahora la intersección de dos set retorna los elementos coincidentes
s1 = {1,2,3}
s2 = {1,2,4}

print(s1.intersection(s2))
# Si usamos una intersección update convertirá el set a sólo los elementos que coincidan
s1.intersection_update(s2)

s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

# disjoint retornará False si existen elementos comunes entre los sets y True si existen
print(s1.isdisjoint(s2))

print(s1.isdisjoint(s3))

# Symmetric differences Para saber cual elemento es el distinto en el 2do set
print(s1.symmetric_difference((s2)))

# Para retornar la unión de los dos sets
a  = s1.union(s2)
print(a)

# Update sets
s1.update(s2)






