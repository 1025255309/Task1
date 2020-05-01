# 将冒泡排序改造成类和函数来实现
class BubbleSort():
    # 定义函数，记得一定要加self这个参数，否则无法被调用
    def bubble_sort(self,list_a):
        # 定义排序次数变量：i
        for i in range(1, len(list_a)):
            # 打印出这是第几次排序
            print("这是第{}次排序".format(i))
            # 定义对比次数变量:j
            for j in range(len(list_a) - i):
                # 打印出这次几次对比
                print("这是第{}次对比".format(j))
                # 使用if条件判断来实现对比相邻元素的大小，满足条件的两个元素互相交换位置
                if list_a[j] > list_a[j + 1]:
                    list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]
        # return确定返回值
        return list_a
# 实例化类
B = BubbleSort()
# 使用关键字传参
list_a = [3, 22, 98, 14, 64, 1, 50, 7, 33]
print(B.bubble_sort(list_a))
#B.bubble_sort(list_a)