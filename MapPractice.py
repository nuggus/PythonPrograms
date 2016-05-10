def squarefunction(val):
    return val ** 2  # power of 2: val^2


# map is used to send a group of inputs to a function and get the results
lis = list(map(squarefunction, range(0, 5)))
# print lis[] created from the returned values of squarefunction(val)
print(lis)
