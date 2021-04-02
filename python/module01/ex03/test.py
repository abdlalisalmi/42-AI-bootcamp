from matrix import Matrix



m1 = Matrix([
    [ 5, 1 ,3], 
    [ 1, 1 ,1], 
    [ 1, 2 ,1]
    ])
m2 = Matrix([
    [ 5, 1 ,3], 
    [ 1, 1 ,1],
    [ 1, 2 ,1]
    ])
print("\nm1 => ", repr(m1))
print("\nm2 => ", repr(m2))

print("\n---------------- Test (m1 * [1, 2, 3]) ----------------")
print(m1 * [1, 2, 3])

print("\n---------------- Test (m1 + m2) ----------------")
print(m1 + m2)

print("\n---------------- Test (m1 + 2) ----------------")
print(m1 * 2)

print("\n---------------- Test (m1 / 2) ----------------")
print(m1 / 2)


print("\n---------------- Test (m1 * m2) ----------------")
print(m1 * m2)
