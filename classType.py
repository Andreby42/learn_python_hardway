##创建自定义类
class Person:
    def set_name(self,name):
        self.name=name;
    def get_name(self):
        return self.name
    def say_hello(self):
        print("hello"+self.name);
    def to_str(self):
        print(self.name())

person=Person();
person.set_name("lily")
print(str(person));
##属性函数与方法
##函数与方法的区别：方法位于类里，有self参数，函数与类同级无self参数
class Mobile:
    def set_os(self,os):
        self.os=os;
    def set_brand(self,brand):
        self.brand=brand;
    def get_os(self):
        return self.os;
    def get_brand(self):
        return self.brand
    def method(self):
        print("I have a mobile"+self.os)
def fuction():
        print("I dont have a Mobile")
sumsung=Mobile();
sumsung.set_os("Android")
sumsung.set_brand("Sumsung")
print(sumsung.method())
print(fuction())
##隐藏 如果想让方法或者属性成为私有，那么只需要让方法或者属性的名称以两个下划线开头即可,只可以在类中进行调用，
##在类外的作用域是调用不到的
class Pc:
    def __brand(self):
        print("this is my pc")
    def print(self):
        print("the pc is")
        self.__brand()
mypc=Pc();
mypc.print()
# mypc._brand()
##指定超类
class Human:
    def body(self,body):
        self.body=body
    def get_body(self):
        print("humanbeing all have body")
    def face(self,face):
        self.face=face
    def get_face(self):
        print("humanbeing all have face")
class Man(Human):#指定human为man的父类
    def dick(self,dick):
        self.dick=dick;
    def _get_dick(self):
        print("man all have a dick or its a monster");
jackChan=Man();
jackChan.dick("big")
jackChan.body("strong")
jackChan.face("handsome")
print(jackChan.get_face(),jackChan.get_body(),jackChan._get_dick())
##判断一个类是否是另一个类的子类 使用 issubclass
print(issubclass(Man,Human))
##如果你有一个类想知道他的基类 那么使用_bases_方法
print(Man.__bases__)
##要确定对象是否是某个类的实例使用isinstance
print(isinstance(jackChan,Man))
##获得当前对象属于哪个类
print(jackChan.__class__)
##多继承暂时不考虑 太麻烦了
class boy(Man):
    ages=14;
    def set_age(self,age):
        self.age=age;
    def get_age(self):
        print("im"+self.age+"old boy");
jim=boy();
jim.ages=14;
jim.set_age("14")
print(boy.__bases__);
attrs=getattr(jackChan,"dick");
print(attrs)
body_attr=hasattr(jackChan,"body")
print(body_attr)
##将对象的指定属性设置为指定的值
setattr(jackChan,"dick","tiny")
print(getattr(jackChan,"dick"))
##返回对象的类型
print(type(jackChan))
###接口与内省

##getattr(object,name[,default]) 获取属性的值 还可以提供默认值
