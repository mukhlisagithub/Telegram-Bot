def bitwiseComplement(n):
    binary = bin(n)
    binary = binary[2:]  # remove the prefix "0b

    complement = ""
    for char in binary:
        if char == "0":
            complement += '1'
        else:
            complement += '0'
    complement = ''.join(complement)
    complement = int(complement, 2)
    return complement

n = 5
print(bitwiseComplement(n))


n = 7
print(bitwiseComplement(n))


n = 10
print(bitwiseComplement(n))