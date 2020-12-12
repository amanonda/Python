a, b, c = map(int, input().split())
d = 0
#bの値も含めて計算するため1を追加している
for i in range(a, b+1):
    if c % i == 0:
        d += 1
print(d)