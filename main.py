def count_exposed_bits(number: int, bits=8) -> int:
    count = 0
    if number < 0:
        number = (1 << bits) + number
    while number > 0:
        count += number & 1
        number >>= 1 
    return count

def main():
    n = int(input())
    result = count_exposed_bits(number=n)
    print(result)

if __name__ == "__main__":
    main()