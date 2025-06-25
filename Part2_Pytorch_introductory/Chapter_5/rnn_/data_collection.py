import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
# fid = 21    #招聘专区模块的ID
# titles21 = []
#
# # 遍历60页
# for pid in tqdm(range(1, 61)):
#     # 获取网页内容
#     url = f'http://dutls.com/ShowForum.asp?PageIndex={pid}&ForumID={fid}'
#     response = requests.get(url)
#     response.raise_for_status()  # 检查请求是否成功
#
#     # 解析HTML内容
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     # 查找所有符合条件的<a>标签
#     a_tags = soup.find_all('a', class_='vam', href=True, target='_blank')
#     for a_tag in a_tags:
#         title = a_tag.text.strip()  # 提取标题文本并去除空格
#         titles21.append(title)
#
#     # 延时1秒，防止请求过快被封IP
#     time.sleep(1)
#
# # 保存标题到文件
# output_path = r'D:/ZhangShijia/learning_content/python学习/PyTorch introductory and hands-on/rnn_/titles21.txt'
# with open(output_path, 'w', encoding='utf-8') as f:
#     for title in titles21:
#         f.write(title + '\n')


fid = 44    #研友专区模块的ID
titles44 = []

# 遍历60页
for pid in tqdm(range(1, 61)):
    # 获取网页内容
    url = f'http://dutls.com/ShowForum.asp?PageIndex={pid}&ForumID={fid}'
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功

    # 解析HTML内容
    soup = BeautifulSoup(response.content, 'html.parser')

    # 查找所有符合条件的<a>标签
    a_tags = soup.find_all('a', class_='vam', href=True, target='_blank')
    for a_tag in a_tags:
        title = a_tag.text.strip()  # 提取标题文本并去除空格
        titles44.append(title)

    # 延时1秒，防止请求过快被封IP
    time.sleep(1)

# 保存标题到文件
output_path = r'D:/ZhangShijia/learning_content/python学习/PyTorch introductory and hands-on/rnn_/titles44.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    for title in titles44:
        f.write(title + '\n')