###字符串
##就介绍下方法吧
str="Hello Python"
#center 字符串居中，
str.center(109)
print(str)
#查找子串，找到就返回第一个的索引
index=str.find("l")
print(index)
##join方法，用于合并序列的元素
list=list("hello pyhon")
str_temple="-"
strnew=str_temple.join(list)
print(strnew)
#lower
str=str.lower();
print(str)
#replace 将指定字符串替换为另一个字符串
str_temple=str.replace("l","P")
print(str_temple)
#split 返回一个序列
strnew=strnew.split("-")
"".join(strnew)
print("".join(strnew))
#strip 去除开头和结尾的空白 不包括中间的空白
str=" "+str;
print(str)
strnew=str.strip()
print(strnew)