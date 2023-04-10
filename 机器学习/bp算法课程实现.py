import numpy as np
import math
import random
import string
import matplotlib as mpl
import matplotlib.pyplot as plt


# random.seed(0)
# 生成区间[a,b]内的随机数
def random_number(a, b):
    return (b - a) * random.random() + a


# 生成一个矩阵，大小为m×n，并且设置默认零矩阵
def makematrix(m, n, fill=0.0):
    a = []
    for i in range(m):
        a.append([fill] * n)
    return a


# sigmoid函数，这里采用tanh
def sigmoid(x):
    return math.tanh(x)


# sigmoid函数的派生函数
def derived_sigmoid(x):
    return 1.0 - x ** 2


# 构造3层bp网络架构
class bpnn:
    def _init_(self, num_in, num_hidden, num_out):
        # 输入层、隐藏层、输出层的节点数
        self.num_in = num_in + 1  # 增加一个偏置节点
        self.num_hidden = num_hidden + 1  # 增加一个偏置节点
        self.num_out = num_out
        # 激活神经网络的所有节点（向量）
        self.active_in = [1.0] * self.num_in
        # 激活神经网络的所有节点（向量）
        self.active_in = [1.0] * self.num_in
        self.active_hidden = [1.0] * self.num_hidden
        self.active_out = [1.0] * self.num_out
        # 创建权重矩阵
        self.weight_in = makematrix(self.num_in, self.num_hidden)
        self.weight_out = makematrix(self.num_hidden, self.num_out)

        # 对权重矩阵赋初值
        for i in range(self.num_in):
            for j in range(self.num_hidden):
                self.weight_in[i][j] = random_number(-0.2, 0.2)
        for i in range(self.num_hidden):
            for j in range(self.num_out):
                self.weight_out[i][j] = random_number(-0.2, 0.2)

        # 建立动量因子（矩阵）
        self.ci = makematrix(self.num. in, self.num_hidden)
        self.co = makematrix(self.num.hidden, self.num_out

# 信号正向传播
def update(self, inputs):
    if len(inputs) != self.num_in - 1:
        raise ValueError('与输入层节点数不符')

    # 数据输入输出层
    for i in range(self.num_in - 1):
        # self.active_in[i] = sigmoid(inputs[i])
        # 或者先在输入层进行数据处理
        # active_in[] 为输入数据的矩阵
        self.active_in[i] = inputs[i]

    # 数据在隐藏层的处理
    for i in range(self.num_hidden - 1):
        sum = 0.0
        for j in range(self.num_in - 1):
            sum = sum + self.active_in[i] * self.weight_in[j][i]
        self.active_hidden[i] = sigmoid(sum)

    # 数据在输出层的处理
    for i in range(self.num_out):
        sum = 0.0
        for j in range(self.num_hidden):
            sum = sum + self.active_hidden[j] * self.weight_out[j][i]
        self.active_out[i] = sigmoid(sum)
    return self.active_out[:]


# 误差反向传播
def errorbackpropagate(self, targets, lr, m):
    # lr为学习率，m为动量因子
    if len(targets) != self.num_out:
        raise valueerror('与输出层节点数不符!')
    # 首先计算输出层的误差
    out_deltas = [0.0] * self.num_out
    for i in range(self.num_out):
        error = targets[i] – self.active_out[i]
        out_deltas[i] = derived_sigmoid(self.active_out[i]) * error
    # 然后计算隐藏层的误差
    hidden_deltas = [0.0] * self.num_hidden
    for i in range(self.num_hidden):
        error = 0.0
        for j in range(self.num_out):
            error = error + out_deltas[j] * self.weight_out[i][j]
        hidden_deltas = derived_sigmoid(self.active_hidden[i]) * error

    # 首先更新输出层权值
    for i in range(self.num_hidden):
        for j in range(self.num_out):
            change = out_deltas[j] * self.active_hidden[i]
            self.weight_out[i][j] = self.weight_out[i][j] + lr * change + m * self.co[i][j]
            self.co[i][j] = change

    # 然后更新输入层权值
    for i in range(self.num_in):
        for j in range(self.num_hidden):
            change = hidden_deltas[j] * self.active_in[i]
            self.weight_in[i][j] = self.weight_in[i][j] + lr * change + m * self.ci[i][j]
            self.ci[i][j] = change

    # 计算总误差
    error = 0.0
    for i in range(len(targets)):
        error = error + 0.5 * (targets[i] - self.active_out[i]) ** 2
    return error


# 测试
def test(self, patterns):
    for i in patterns:
        print(i[0], '->', self.update(i[0]))


# 权重
def weights(self):
    print('输入值权重')
    for i in range(self.num_in):
        print(self.weight_in[i])
    print('输出值权重')
    for i in range(self.num_hidden):
        print(self.weight_out[i])


def train(self, patterns, itera=100000, lr=0.1, m=0.1):
    for i in range(itera):
        error = 0.0
        for j in patterns:
            inputs = j[0]
            targets = j[1]
            self.update(inputs)
            error = error + self.errorbackpropagate(targets, lr, m)


# 示例
def demo():
    patt = [
        [[1, 2, 5], [0]],
        [[1, 3, 4], [1]],
        [[1, 6, 2], [1]],
        [[1, 5, 1], [0]],
        [[1, 8, 4], [1]]
    ]
    # 创建神经网络，3个输入节点，3个隐藏层节点，1个输出层节点
    n = BPNN(3, 3, 1)
    n.train(patt)  # 训练神经网络
    n.test(patt)  # 测试神经网络
    n.weights()  # 查阅权重值


If__name__ == '__main__':
    demo()
