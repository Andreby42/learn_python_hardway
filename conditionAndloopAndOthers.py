num = int(input("enter a num"))
if num > 0:
    print("positive")
elif num < 0:
    print("nagetive")
else:
    print("num is zero")
##代码块嵌套
name = input("what is your name")
if name.endswith("Gumby"):
    if name.startswith("anderson"):
        print("hello Mr.Anderson")
    elif name.startswith("Ms."):
        print("Hello Ms")
    else:
         print("hello andy")
else:
    print("Hello GUMBY")
##更复杂的对象
##x is y  x和y是同一个对象
## x is not y x和y 不是同一个对象
## x in y x是容器如序列y的成员元素
##x not in y x不是y容器的成员元素
nam = input("What is your name？")
if 's' in name:
    print("your name constains letter s")
else:
    print("your name does not contain letter s")
ord("a")
## 布尔运算符
number=int(input("plz enter a num between 1 and 10 :"))
if number <=10:
 if number >=1:
     print("Great")
 else:
     print("Wrong")
else:
 print("Wrong")
##断言 assert 来做检查点
age = 10
assert 0<age<100
age=-1
##assert 0<age<100
##循环
##while 循环
##while True:
##    print("Hello Mr.anderson")
z=1
while z<=100:
    print(z)
    z += 1
## for循环
words=["this","is","a","ex","parrot"]
for word in words:
    print(word)

##关于迭代的内置函数 range
range(0,10)
list(range(0,10))
for number in range(1,101):
    print(number)
##迭代字典
dic={"a":1,"b":2,"c":3,"d":4}

for key,value in dic.items():
    print(key,'corresponds to ',value)
##一些py的迭代工具
namess=['andy','candy','booby','dc']
ages=[1,3,5,6,7,8]
for i in range(len(namess)):
    print(namess[i],'is',ages[i],'old')
##使用zip进行迭代
list(zip(namess,ages))

for name,age in zip(namess,ages):
    print(name,'is zip',age,'years old')
##迭代时获取索引 使用enumerate
for index,name in  enumerate(namess):
    if 'andy' in namess:
            namess[index]='luca'
print(namess)
##False None  0 "" ()] {} 都为false
## == 用来比较两个对象是否相等，is用来比较两个对象的值是否相同
## in 用来表示  a 是否在b中


