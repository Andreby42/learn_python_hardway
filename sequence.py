
##sequence 序列容器不限定元素类型
sequen=["andy",42];
#通过索引下标取序列的元素
print(sequen[0]);
##切片slicing,用来访问序列中特定范围内的元素,起始索引和结束索引使用冒号进行分割
sequen.append("is");
sequen.append("a");
sequen.append("boy");
sequen.append("it");
sequen.append("is");
sequen.append("a");
sequen.append("good");
sequen.append("day");
print(sequen.__len__())
sliceing=sequen[0:3];
#如果起始索引为0的话可以省略
sliceing=sequen[:3]
print(sliceing)
#切片从列表末尾开始分割的话，那么用负号
sliceing=sequen[-3:-1]
print(sliceing)
#若要复制索引 那么直接:就可以
sliceing=sequen[:]
print(sliceing)
# 步长 步长如果指定参数，那么不能为0 ，可以为负数，意思为从右向左提取元素
#第三个参数为步长，意思为每隔1个元素提取
sliceing=sequen[1:10:2]
print(sliceing)
#序列相加 使用加号进行拼接序列
another_sequen=["what","a","good","day","!"];
third_sequen=sequen+another_sequen;
print(sequen+another_sequen);
#序列乘法,来获取一个原序列N倍元素的新序列
third_sequen=sequen*5;
print(third_sequen)
#None 空列表，及序列初始化
#空列表使用[]来表示，但是如果要创建一个指定长度的空序列的话 那么使用None
third_sequen=[];
print(third_sequen)
third_sequen=[None]*10;
print(third_sequen)
#成员资格，
#检查元素是否在序列中 使用 element in sequence
element="a";
print(element in another_sequen);
#序列长度，最小值，最大值
lenth=another_sequen.__len__();
print(lenth)
lenth=len(another_sequen)
print(lenth)
max=max(another_sequen)
print(max)
min=min(another_sequen)
print(min)


