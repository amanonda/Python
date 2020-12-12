w, h, x, y, r = map(int, input().split())
if(w < (x + r) or h < (y + r) or x < 0 or y < 0):
    print('No')
else:
    print('Yes')