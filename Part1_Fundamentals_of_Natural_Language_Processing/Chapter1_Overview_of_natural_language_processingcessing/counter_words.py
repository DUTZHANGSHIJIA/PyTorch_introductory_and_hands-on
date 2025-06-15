from collections import Counter
f = open('蛊真人.txt', 'r', encoding='utf-8')
txt = f.read()
f.close()

# 统计单个字符的频率
cnt = Counter(txt)

# 统计多个字符词语的频率
# 输入词语长度并验证
while True:
    try:
        word_length = int(input("请输入要统计的词语长度（如2表示两个字符的词语）："))
        if word_length <= 0:
            raise ValueError("词语长度必须是正整数！")
        break
    except ValueError:
        print("输入无效，请输入一个正整数！")
words = [txt[i:i+word_length] for i in range(len(txt) - word_length + 1)]
word_cnt = Counter(words)

# 合并单字符和多字符统计结果
cnt.update(word_cnt)

# 查询特定词语
query = input("请输入要查询的词语：")
print(f"词语 '{query}' 出现的次数为：{cnt[query]}")

# 可视化单字符统计结果
char_list = []
for char in cnt:
    if len(char) == 1 and char in "\u3000\n。，：！!“”？《》； （）-——、^……【】":
        continue
    if len(char) == 1:
        char_list.append([cnt[char], char])

char_list.sort(reverse=True)  # 降序排列

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