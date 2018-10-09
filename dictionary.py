from copy import  deepcopy
###字典 键值对映射容器，使用冒号进行分割键值
##创建使用字典
#dict函数
list=[("name","andy"),("age","14")]
dic_1=dict(list)
print(dic_1["name"])
#使用参数进行调用函数
dict_2=dict(name="andrew",age="14")
print(dict_2['name'])
#基本操作之len
lenth=len(dict_2)
print(lenth)
#通过key取得value，或者进行赋值
print(dict_2["age"])
dict_2["age"]="15";
print(dict_2["age"])
#删除key为xx的项
del (dict_2["age"])
print(dict_2)
#同列表相同 空字典进行指定key赋值的时候 会报错那么这时候就需要进行使用None初始化了
##字典方法
#clear 清楚所有项 返回一个None 或者说没有返回
dict_2.clear()
print(dict_2)
#copy 浅复制
dict_copy=dic_1.copy()
print(dict_copy)
#深赋值 引入deepcopy 模块
dc=deepcopy(dic_1)
print(dc)
#创建一个新的字典 其中包含指定的键并且每个键的对应的值都是None
dict_4={}.fromkeys(["name","sex","age"]);
print(dict_4)
#get 获取指定key 如果访问字典中没有的项那么会报错
dict_4["name"]="ok"
name=dict_4.get("name")
print(name)
#item 获得一个包含所有字典项目的列表,列表的排序顺序不确定，返回一个字典试图
dict_list=dict_4.items()
print(dict_list)
#keys 获得所有keys的字典视图
list=dict_4.keys()
print(list)
#pop 获取对应的value，删除并返回这个value的值 如果不指定的话 弹出最后一个？
itemelement=dict_4.pop("name")
print(itemelement)
print(dict_4)
#popitem 随机删除一个字典项，因为字典项的顺序是不确定的，没有最后一个元素的概念
itemelement=dict_4.popitem()
print(itemelement)
#setdefault 获取指定键的值，当字典不包含指定项的 时候 在字典中添加指定的键-值对,但当值为None的时候会默认为存在值，再setdefault也不起作用了
dict_4.setdefault("sex","male")
print(dict_4)
dict_4.setdefault("name","andy")
print(dict_4)
#update 更新字典，使用一个字典中的项，更新另一个字典
dict_update={"name":"luca"}
dict_4.update(dict_update)
print(dict_4);
#values 发怒hi一个有字典中的值组成的字典视图，可能包含重复元素
values=dict_4.values();
print(values)