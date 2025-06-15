#count the number of elements in an iterable object
from collections import Counter
f = open('蛊真人.txt', 'r', encoding='utf-8')
txt = f.read()
f.close()

cnt = Counter(txt)
char_list = []
for char in cnt:
    if char in "\u3000\n。，：！!“”？《》； （）-——、^……【】":
        continue
    char_list.append([cnt[char], char])

char_list.sort(reverse=True) #降序排列

for char in char_list:
    print(char[1], char[0])  #打印字符和对应的数量

import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')
x = []
y = []
for i, char_cnt in enumerate(char_list):
    x.append(i)
    y.append(char_cnt[0])
plt.axis((0, 100, 0, 300000))
plt.bar(x[:100], y[:100], width=1)
plt.show()