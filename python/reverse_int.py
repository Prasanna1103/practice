import math

def main():
    num = 7234
    print(f"original number: {num}")

    reversed = reverse(num)
    #resersed *= 3
    print(f"reversed number: {reversed}")

def reverse(num):
    result = 0
    while num > 0:
        a = num%10
        result = result*10+a
        num = math.floor(num / 10)
        print(f"a = {a}, num = {result}")
    return result

if __name__ == '__main__':
    main()
