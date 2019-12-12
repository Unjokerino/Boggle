# -*- coding: utf-8 -*-

import time
import codecs
import json
import sys

NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),        (0, 1),
             (1, -1), (1, 0), (1, 1)]

usedList = []  # TODO: Исправить этот костыль
gridcoo = []


def solve(grid):
    start_time = time.time()
    results = []

    words = set(word.rstrip('\n').strip().lower()
                for word in codecs.open('dictionary.txt', encoding='UTF-8') if len(word) >= 3)

    # print('Загрузка словаря закончена: %f' % (time.time() - start_time))
    prefix_set = set(word[:i] for word in words for i in range(1, len(word)+1))
    # print("Создания префикс сета окончено: %f" % (time.time() - start_time))
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            results += find_words(grid, words, prefix_set,
                                  grid[y][x], y, x, set([y, x]), set((str(y)+str(x))))
    # print('Поиск слов закончен: %f' % (time.time() - start_time))
    return set(results)


usedList = []
foundDic = {}


def find_words(grid, words, prefix_set, current, y, x, used, path):
    found = []
    if current not in prefix_set:
        return found
    used.add((y, x))
    path.add((str(y)+str(x)))

    for dy, dx in NEIGHBORS:
        ny, nx = y + dy, x + dx

        if in_grid(grid, ny, nx) and (ny, nx) not in used:
            used.add((ny, nx))
            path.add((str(ny)+str(nx)))
            found.extend(find_words(grid, words, prefix_set, current +
                                    grid[ny][nx], ny, nx, used, path))
            used.remove((ny, nx))
            path.remove((str(ny)+str(nx)))

    if current in words:
        if len(current) > 1:
            foundDic.update({current: list(path)})
            found.append(current)
            usedList.append(list(used))

    return list(found)


def in_grid(grid, y, x):
    return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[y])


grid = []
seq = sys.argv[1]
length = 5
dividedGrid = map(''.join, zip(*[iter(seq)]*length))
for gridS in dividedGrid:
    grid.append(gridS.lower())
result = solve(grid)
f = open("result.txt", "w")
listRsult = []
for word in sorted(result):
    listRsult.append(word)

# TODO:Этот костыль тож исправить
listRsult.sort(key=len, reverse=True)

jsonList = json.dumps(listRsult)
foundDic = json.dumps(foundDic)
print(foundDic)
for word in listRsult:
    f.write(word+'\n',)
f.close()
