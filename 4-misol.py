# 2-misol
def decorator(func):
    def wrapper(a):
        b = []
        for k in range(1, len(a)+1):
            b.append(sum(a[:k]) / k)
        return b
    return wrapper



@decorator
def salom_ber(a):
    return a  
a = [2, 4, 6, 8]
b = salom_ber(a)
print(b)  
