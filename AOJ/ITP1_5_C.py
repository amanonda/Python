while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:break
    for i in range(h):
        #iは0から始まる
        print(('#.' * w)[i % 2:][:w])
    print()