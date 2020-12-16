#バブルソートはバラバラに並んでいるデータを隣り合う数で比べて
#昇順または降順に並べ直すアルゴリズム
def bubble_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 -i):
            if collection[j] > collection[j + 1]:
                swa