def positive_to_binary(number: int) -> list[int]:
    if (number < 0):
        return None
    
    bits = []
    while number > 0:
        bits.append(number % 2) 
        number //= 2
    return bits[::-1]
    
def to_binary(number: int) -> list[int]:
    if number >= 0:
        return positive_to_binary(number)

    abs_number = abs(number)
    bits = positive_to_binary(abs_number)
    
    inverted_bits = []
    for bit in bits:
        inverted_bits.append(1 - bit)
    
    flag = 1
    for i in range(len(inverted_bits) - 1, -1, -1):
        if (inverted_bits[i] == 0 and flag):
            inverted_bits[i] = 1
            flag = 0
        elif(inverted_bits[i] == 1 and flag):
            inverted_bits[i] = 1 
        else:
            break

    return inverted_bits
    
def count_exposed_bits(number: int) -> int:
    resulted_bits = to_binary(number)
    exposed_bits_quantity = resulted_bits.count(1)
    if number < 0:
        exposed_bits_quantity += 1
    return exposed_bits_quantity

def main():
    number = int(input())
    print(count_exposed_bits(number))


if __name__ == "__main__":
    main()        