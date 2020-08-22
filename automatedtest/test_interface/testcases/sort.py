# list_a = [2,9,6,4,3,91,8,71,54]
# # 利用i遍历列表各元素
# for i in range (len(list_a)-1):
#     # 打印对比次数，可省略，初学者建议加上，提高代码可读性
#     print("这是第{}次排序".format(i))
#         # 定义j为列表索引
#     for j in range(len(list_a)-i-1):
#             # 打印对比次数，可省略，初学者建议加上，提高代码可读性
#             print("这是第{}次对比".format(j))
#             # 使用if条件判断来实现对比相邻元素的大小，满足条件的两个元素互相交换位置
#             if list_a[j]>list_a[j+1]:
#                 list_a[j], list_a[j+1]=list_a[j+1], list_a[j]
# #打印这个列表
#
# print(list_a)

# y=lambda x,y,z:x+y+z
# print(y(2,3,4))

list1=[1,2,3]
y=lambda x:x*x

print([y(x) for x in list1] )