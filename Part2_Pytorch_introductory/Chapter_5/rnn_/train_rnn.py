# 定义两个list分别存放两个板块的帖子数据
academy_titles = []
job_titles = []
with open('academy_titles.txt', encoding='utf8') as f:
    for l in f:  # 按行读取文件
        academy_titles.append(l.strip( ))  # strip 方法用于去掉行尾空格
with open('job_titles.txt', encoding='utf8') as f:
    for l in f:  # 按行读取文件
        job_titles.append(l.strip())  # strip 方法用于去掉行尾空格

char_set = set()
for title in academy_titles:
    for ch in title:
        char_set.add(ch)
for title in job_titles:
    for ch in title:
        char_set.add(ch)
print(len(char_set))
#
import torch
char_list = list(char_set)
n_chars = len(char_list) + 1 # 加一个 UNK
#
def title_to_tensor(title):
    tensor = torch.zeros(len(title), dtype=torch.long)
    for li, ch in enumerate(title):
        try:
            ind = char_list.index(ch)
        except ValueError:
            ind = n_chars - 1
        tensor[li] = ind
    return tensor
#
import json
with open('char_list', 'w') as f:
    json.dump(char_list, f)

import torch.nn as nn

class RNN(nn.Module):
    def __init__(self, word_count, embedding_size, hidden_size, output_size):
        super(RNN, self).__init__()

        self.hidden_size = hidden_size
        self.embedding = torch.nn.Embedding(word_count, embedding_size)
        self.i2h = nn.Linear(embedding_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(embedding_size + hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input_tensor, hidden):
        word_vector = self.embedding(input_tensor)
        combined = torch.cat((word_vector, hidden), 1)
        hidden = self.i2h(combined)
        output = self.i2o(combined)
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)


embedding_size = 100
n_hidden = 128
n_categories = 2
rnn = RNN(n_chars, embedding_size, n_hidden, n_categories)

input_tensor = title_to_tensor(academy_titles[0])
print('input_tensor:\n', input_tensor)

embedding_size = 100
n_hidden = 128
n_categories = 2
rnn = RNN(n_chars, embedding_size, n_hidden, n_categories)

hidden = rnn.initHidden()
output, hidden = rnn(input_tensor[0].unsqueeze(dim=0), hidden)
print('output:\n', output)
print('hidden:\n', hidden)
print('size of hidden:\n', hidden.size())

def run_rnn(rnn, input_tensor):
    hidden = rnn.initHidden()
    for i in range(input_tensor.size()[0]):
        output, hidden = rnn(input_tensor[i].unsqueeze(dim=0), hidden)
    return output

all_data = []
categories = ["考研考博", "招聘信息"]

for l in academy_titles:
    all_data.append((title_to_tensor(l), torch.tensor([0], dtype=torch.long)))
for l in job_titles:
    all_data.append((title_to_tensor(l), torch.tensor([1], dtype=torch.long)))

    import random

    random.shuffle(all_data)
    data_len = len(all_data)
    split_ratio = 0.7
    train_data = all_data[:int(data_len * split_ratio)]
    test_data = all_data[int(data_len * split_ratio):]
    print("Train data size: ", len(train_data))
    print("Test data size: ", len(test_data))

def train(rnn, criterion, input_tensor, category_tensor):
    rnn.zero_grad()
    output = run_rnn(rnn, input_tensor)
    loss = criterion(output, category_tensor)
    loss.backward()

    # 根据梯度更新模型的参数
    for p in rnn.parameters():
        p.data.add_(p.grad.data, alpha=-learning_rate)

    return output, loss.item()

def evaluate(rnn, input_tensor):
    with torch.no_grad():
        hidden = rnn.initHidden()
        output = run_rnn(rnn, input_tensor)
        return output

from tqdm import tqdm
epoch = 20
embedding_size = 200
n_hidden = 10
n_categories = 2
learning_rate = 0.005
rnn = RNN(n_chars, embedding_size, n_hidden, n_categories)
criterion = nn.NLLLoss()
loss_sum = 0
all_losses = []
plot_every = 100
for e in range(epoch):
    for ind, (title_tensor, label) in enumerate(tqdm(train_data)):
        output, loss = train(rnn, criterion, title_tensor, label)
        loss_sum += loss
        if ind % plot_every == 0:
            all_losses.append(loss_sum / plot_every)
            loss_sum = 0
    c = 0
    for title, category in tqdm(test_data):
        output = evaluate(rnn, title)
        topn, topi = output.topk(1)
        if topi.item() == category[0].item():
            c += 1
    print('accuracy', c / len(test_data))

c = 0
l1 = []
l2 = []
for title, category in tqdm(test_data):
    output = evaluate(rnn, title)
    topn, topi = output.topk(1)
    l1.append(topi.item())
    l2.append(category[0].item())
    if topi.item() == category[0].item():
        c += 1
print('accuracy', c / len(test_data))

print(l1[:40])
print(l2[:40])

c = 0
for title, category in tqdm(test_data):
    output = evaluate(rnn, title)
    topn, topi = output.topk(1)
    if topi.item() == category[0].item():
        c += 1
print('accuracy', c / len(test_data))


import matplotlib
# 选择一种后端（按优先级尝试）
matplotlib.use('TkAgg')   # 首选
import matplotlib.pyplot as plt

plt.figure(figsize=(10,7))
plt.ylabel('Average Loss')
plt.plot(all_losses[1:])
plt.show()

#保存模型
torch.save(rnn, 'rnn_model.pkl')
# #加载模型
# rnn = torch.load('rnn_model.pkl')
#
#保存词表
with open('char_list', 'w') as f:
    json.dump(char_list, f)
# #加载词表
# with open('char_list', 'r') as f:
#     char_list = json.load(f)

def get_category(title):
    title = title_to_tensor(title)
    output = evaluate(rnn, title)
    topn, topi = output.topk(1)
    return categories[topi.item()]

def print_test(title):
    print('%s\t%s' % (title, get_category(title)))

print_test('2024年考研英语二作文预测题目')
print_test('考研心得')
print_test('考博士需要哪些条件')
print_test('2024年秋季招聘信息')
print_test('2024年春季招聘信息')
print_test('校招offer比较')
print_test('急求自然语言处理工程师')