"""
使用列表推导式写下面这个算法题
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]
提示：
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。
"""
import math  # 导入math库
def nondecrease_sort(list_a):  # 定义一个非递减排序函数
    b=sorted(i**2 for i in list_a)  # 使用列表推导式，先做列表中数字平方，再排序，并将排序后的列表赋值给变量b
    # for i in list_a:
    #     i=i**2
    # b=sorted(list_a)
    print(b)  # 打印b
nondecrease_sort(list_a = [-4, -1, 0, 3, 10])  # 调用函数并传参
nondecrease_sort(list_a = [-7, -3, 2, 3, 11])  # 调用函数并传参