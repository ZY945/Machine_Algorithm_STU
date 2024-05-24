# 四部曲
https://victorzhou.com/series/neural-networks-from-scratch/
认识神经网络
原文:https://victorzhou.com/blog/intro-to-neural-networks/
翻译:https://zhuanlan.zhihu.com/p/377513272

1. 神经元是什么
2. 神经网络是由多个神经元组成
3. 激活函数(常用的固定函数)---起点公式
4. 损失函数----用来计算真实结果和预测结果的差异---不断训练神经网络来进行提升
5. 反向传播与均方误差
# 个人感想
## 单个神经元
入门：两个输入通过一个黑盒，输入一个对应的值
例如二元函数。y=ax1+bx2+c
a和b和c是所选函数的，自变量(这里不知道是计算出来还是选择的，反正在该函数的时候是已知的)
输入x1和x2，然后得出y的值，接着把y放进f(y)得出输出的值
## 神经网络--多个神经元
但是不知道两个输出如何处理为一个，可能最后再次处理f(x)
递归神经网络RNN(未开始)
https://victorzhou.com/blog/intro-to-rnns/
# nupmy
```python
np.dot
```