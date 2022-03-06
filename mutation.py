# Tuple are immutable but an element within a tuple can be mutable
tuple = (1, 2, 3, 4, [5, 6, 7], 8, 9)
tuple[4][1] = 0
print(tuple)
