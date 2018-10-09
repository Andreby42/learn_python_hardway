###列表 好像lisp啊 因为这个东西是python的主力啊
##基本列表方法
#列表函数,list() 可以将任何序列作为list的参数
list_1=list("hello,python")
print(list_1)
list_2=list(list_1)
print(list_2)
#给元素赋值 直接使用索引角标进行赋值
list_example=list("hello");
list_example[1]="ok";
print(list_example)
#删除元素 使用del语句
del list_example[1]
print(list_example)
list_example[1]="e";
print(list_example)
#给切片赋值
list_4=list("Peral");
list_4[1:]=list("ython")
print(list_4)
#也可以在不改变原有切片内容的情况下，进行添加元素
list_5=list("good");
str=list("is");
list_4=list_4+str
print(list_4)
#这里进行了添加元素，使用 ：
list_4[len(list_4):len(list_4)]=list_5;
print(list_4)
##列表方法
#append方法
list_6=[1,2,3,4,5]
list_6.append(6);
list_copy=list_6.copy();
print(list_6)
#clear方法
list_6.clear();
print(list_6)
#copy
print(list_copy)
#count() 计算指定元素出现了多少词
list_copy.append(6);
list_copy.append(6);
list_copy.append(6);
list_copy.append(6);
count=list_copy.count(6);
print(count)
#extend 扩展 ，这个方法很有用 可以将两个list进行追加，a.expend(b)，和常规的序列拼接的区别是
#常规的使用+进行拼接返回的是一个全新的list 而 使用expend是在a上进行扩展，所以扩展的内容在a列表上
list_expend_1=list("Python");
list_expend_2=list("is");
list_expend_3=list("good")
list_expend_1.extend(list_expend_2);
list_expend_1.extend(list_expend_3)
print(list_expend_1)
#index 返回在列表中查找指定值第一次出现的索引
index=list_expend_1.index("g")
print(index)
#insert 将一个对象插入列表
list_expend_1.insert(len(list_expend_1),"?")
print(list_expend_1)
#也可以使用切片赋值获得与insert相同的效果,但是可读性不如insert
list_expend_1[len(list_expend_1):len(list_expend_1)]="！";
print(list_expend_1)
#pop 从列表中删除一个元素，并返回这一元素 如果不传参数就是默认最后一个元素，传参就是指定索引位置的元素进行pop
#pop是唯一既修改列表又返回非none值的列表方法
element=list_expend_1.pop()
print(element)
print(list_expend_1)
#remove 删除第一个为指定值的元素
list_expend_1.extend("!");
print(list_expend_1)
list_expend_1.remove("!")
print(list_expend_1)
#reverse 反转
list_expend_1.reverse()
print(list_expend_1)
#sort 对列表就地排序 a.sort() sorted(a) sorted返回一个新的列表 不在原列表进行处理
list_copy.reverse()
print(list_copy)
list_copy.sort()
print(list_copy)
list_copy.reverse()
print(list_copy)
sorted_list=sorted(list_copy)
print(sorted_list)
#高级排序 sort方法接受两个可选参数 key和reverse  key的意思为按什么条件进行排序，reverse的意思为是否进行反转
list_expend_1.sort(key=len)
print("条件排序",list_expend_1)
list_copy.sort(reverse=True)
print("反转排序",list_copy)