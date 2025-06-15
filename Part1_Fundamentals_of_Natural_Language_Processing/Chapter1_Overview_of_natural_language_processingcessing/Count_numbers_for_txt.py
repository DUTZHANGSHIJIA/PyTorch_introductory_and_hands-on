import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter

def select_file():
    file_path = filedialog.askopenfilename(title="请选择一个TXT文件", filetypes=[("Text files", "*.txt")])
    if not file_path:
        messagebox.showerror("错误", "未选择文件！")
        return
    file_path_var.set(file_path)

def process_file():
    file_path = file_path_var.get()
    if not file_path:
        messagebox.showerror("错误", "请先选择文件！")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            txt = f.read()
    except Exception as e:
        messagebox.showerror("错误", f"文件读取失败：{e}")
        return

    try:
        word_length = int(word_length_var.get())
        if word_length <= 0:
            raise ValueError("词语长度必须是正整数！")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的词语长度！")
        return

    # 统计单个字符和多个字符的频率
    cnt = Counter(txt)
    words = [txt[i:i+word_length] for i in range(len(txt) - word_length + 1)]
    word_cnt = Counter(words)
    cnt.update(word_cnt)

    # 查询特定词语并验证长度
    query = query_var.get()
    if query:
        if len(query) != word_length:
            messagebox.showerror("错误", f"查询词语的长度（{len(query)}）与统计的词语长度（{word_length}）不一致！")
            return
        query_count = cnt[query]
        messagebox.showinfo("查询结果", f"词语 '{query}' 出现的次数为：{query_count}")

    # 可视化单字符统计结果
    char_list = []
    for char in cnt:
        if len(char) == 1 and char in "\u3000\n。，：！!“”？《》； （）-——、^……【】":
            continue
        if len(char) == 1:
            char_list.append([cnt[char], char])

    char_list.sort(reverse=True)  # 降序排列

# 创建主窗口
root = tk.Tk()
root.title("词频统计工具")

# 文件选择
file_path_var = tk.StringVar()
tk.Label(root, text="选择文件：").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=file_path_var, width=40).grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="浏览", command=select_file).grid(row=0, column=2, padx=5, pady=5)

# 输入词语长度
word_length_var = tk.StringVar()
tk.Label(root, text="词语长度：").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=word_length_var, width=10).grid(row=1, column=1, padx=5, pady=5)

# 输入查询词语
query_var = tk.StringVar()
tk.Label(root, text="查询词语：").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=query_var, width=20).grid(row=2, column=1, padx=5, pady=5)

# 开始处理按钮
tk.Button(root, text="开始统计", command=process_file).grid(row=3, column=0, columnspan=3, pady=10)

# 运行主循环
root.mainloop()