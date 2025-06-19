import torch

# #4.1.1
# #1
# t = torch.tensor([[1,2,3],[4,5,6]])
# print(t,t.shape,t.dtype)
# t2 = torch.Tensor([[1,2,3],[4,5,6]])
# print(t2,t2.shape,t2.dtype)
#
# #2、创建全0、全1或随机数张量
# rand_tensor = torch.rand(2, 3)
# ones_tensor = torch.ones(2, 3)
# zeros_tensor = torch.zeros(2, 3)
# print(rand_tensor, rand_tensor.shape, rand_tensor.dtype)
# print(ones_tensor, ones_tensor.shape, ones_tensor.dtype)
# print(zeros_tensor, zeros_tensor.shape, zeros_tensor.dtype)
#
# # 4.1.2张量的变换
# # 1.拼接与堆叠
# t1 = torch.tensor([1, 2, 3])
# t2 = torch.tensor([4, 5, 6])
# t3 = torch.cat([t1, t2], dim=0)  # 在第0维拼接
# print(t3)
# t1 = torch.tensor([[1, 2, 3],[1, 2, 3]])
# t2 = torch.tensor([[4, 5, 6],[4, 5, 6]])
# t3 = torch.cat([t1, t2], dim=0)  # 在第0维拼接
# t4 = torch.cat([t1, t2], dim=1)  # 在第1维拼接（仅当t1和t2是二维张量时有效）
# print(t3)
# print(t4)
#
# t1 = torch.tensor([[1, 2, 3],[1, 2, 3]])
# t2 = torch.tensor([[4, 5, 6],[4, 5, 6]])
# t3 = torch.stack([t1, t2], dim=0)  # 在第0维堆叠
# t4 = torch.stack([t1, t2], dim=1)  # 在第1维堆叠
# t5 = torch.stack([t1, t2], dim=2)  # 在第2维堆叠
# print(t3, t3.shape, t3.dtype)
# print(t4, t4.shape, t4.dtype)
# print(t5, t5.shape, t5.dtype)
#
# # 2.切分
# t = torch.tensor([1, 2, 3, 4, 5])
# print(torch.chunk(t, 1))
# print(torch.chunk(t, 2))
# print(torch.chunk(t, 3))
# print(torch.chunk(t, 4))
# print(torch.chunk(t, 5))
# # print(torch.chunk(t, 6))  # 不能分成6份，报错
#
# t = torch.tensor([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
# print(torch.split(t, 2, 0))
# print(torch.split(t, 2, 1))
#
# # 3.变形
# t = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(t.reshape(3, 3))  # 将一维张量变为三行三列的二维张量
# print(t.reshape(3, -1)) # -1表示自动计算 但只能使用一个-1
#
# # 4.交换维度
# t = torch.tensor([[1, 2, 3], [4, 5, 6]])
# t2 = torch.transpose(t, 0, 1)  # 交换第0维和第1维
# print(t, t.shape, t.dtype)
# print(t2, t2.shape, t2.dtype)
#
# # 5.squeeze和unsqueeze
# t = torch.tensor([[1, 2, 3], [4, 5, 6]])
# t2 = torch.unsqueeze(t, 0)  # 在第0维增加一个大小为1的维度
# t3 = torch.unsqueeze(t, 1)  # 在第1维增加一个大小为1的维度
# t4 = t2.squeeze()
# print(t, t.shape, t.dtype)
# print(t2, t2.shape, t2.dtype)
# print(t3, t3.shape, t3.dtype)
# print(t4, t4.shape, t4.dtype)
#
# # 6.expand
# x = torch.tensor([[[0.5, 0.1, 0.3]], [[0.8, 0.2, 0.1]]])
# print(x, x.shape)
# y = x.expand(2, 8, 3)
# print(y, y.shape)
#
# # 7.repeat
# x = torch.tensor([[[0.5, 0.1, 0.3]], [[0.8, 0.2, 0.1]]])
# print(x, x.shape)
# y = x.repeat(2, 2, 2)  # 重复2次，2次，2次
# print(y, y.shape)

# # 4.1.3张量的索引
# t = torch.tensor([[1, 2, 3], [4, 5, 6]])
# print(t[1])
# print(t[1][2])
# print(t[1][2].item())

# t = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(t[:, 1])
# print(t)
# t[:, 1] = t[:, 2]
# print(t)

# # 4.1.4张量的运算
# t1 = torch.tensor([[1, 2, 3]])
# t2 = t1 + 1
# t3 = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# t4 = t1 + t3
# print(t2)
# print(t4)