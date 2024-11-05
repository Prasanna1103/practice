import math

def reverse(num):
    result = 0
    while num > 0:
        a = num%10
        result = result*10+a
        num = math.floor(num / 10)
        print(f"a = {a}, num = {result}")
    return result

num = 7234
print(f"original number: {num}")

reversed = reverse(num)
#resersed *= 3
print(f"reversed number: {reversed}")
