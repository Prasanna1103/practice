import math

def reverse(num):
    a = num%10
    print("a = ", a)
    b = math.floor((num / 10)%10)
    print("b = ", b)
    c= math.floor((num/100)%10)
    print("c = ", c)
    return a*100 + b*10 + c

num = 7234
print(f"original number: {num}")

reversed = reverse(num)
#resersed *= 3
print(f"reversed number: {reversed}")
