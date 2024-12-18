def to_binary(n):
    return bin(n)[2:]  # bin() returns '0b' prefix, we slice it off

#test
print(to_binary(10)) #output: 1010