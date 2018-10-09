###元组
#空元组使用() 来表示
tuple_1=(1,2,3,"test")
element_3=tuple_1[3]
print(element_3)
#只包含一个元素的tuple,即使只有一个元素那么也要加逗号
tuple_2=(42,)
print(tuple_2)
#将tuple转为list
list=list(tuple_1)
print(list)
#将序列转为元组
tuple_3=tuple(list)
print(tuple_3)
###小结
##序列 是一种数据结构  列表字符串元组都属于序列，其中列表是可变的，元组和字符串是不可变的(一旦创建，内容就是固定的)
##要访问序列的一部分 使用切片，提供两个指定切片开始和结束位置的索引，
##成员资格 使用in查看特定的值是否在序列中
##方法 就不说了