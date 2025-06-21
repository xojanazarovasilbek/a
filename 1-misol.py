# 1-misol
def generator(a):
    for i in a:
        yield i
a = str(input("so'z kiriting"))
for harf in generator(a):
    print(harf)
