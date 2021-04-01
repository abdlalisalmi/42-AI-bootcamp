from vector import Vector



v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector([0.0, 1.0, 2.0, 3.0])

print("V1", v1.values)
print("V2", v2.values)

print("\nTest repr(v1): -----------------------")
print(repr(v1))

print("\nTest v1 - 2 : -----------------------")
print(v1 - 2)

print("\nTest v1 + v2 : -----------------------")
print(v1 + v2)

print("\nTest v1 * v2 : -----------------------")
print(v1 * v2)

print("\nTest v1 / 2 : -----------------------")
print(v1 / 2)