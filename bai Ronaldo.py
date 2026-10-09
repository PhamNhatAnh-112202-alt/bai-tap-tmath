n, m = input().split()
n = int(n)
m = int(m)
if n>m:
    print(m,(n-m)//2)
else:
    print(n,(m-n)//2)

