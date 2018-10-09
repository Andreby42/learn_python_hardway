## 函数 抽象
#斐波那契数列
##函数体要写在调用之前
nums=int(input("enter a num"))
def fibs(nums):
    ##为函数编写文档
    'a fibs function'
    list = [];
    for i in range(nums):
            if i==0 or i==1:
                list.append(1)
            else:
                list.append(list[i-2]+list[i-1]);
    print(list)
fibs(nums);
##打印函数文档
doc=fibs.__doc__
print(doc)
##return 只是为了结束语句
def my_introduce(name,age,sex):
    print("myname is",name,sex,"im",age,"old");
##多参数的函数 在调用时候可以指定 函数参数
my_introduce(name="xiaohong",age="14",sex="male");
## java 中传入多个参数 是这样的 如 ...String 这代表了一个string的数组 python中这么干,叫做收集参数
def test(name1,name2,name3):
    print(name1,name2,name3)
def test1(*params):
    print(params)
test("a","b","c")
test1("ABC")