###魔法方法。特性和迭代器
##构造函数
class Person:
    def __init__(self,name,age,gender):
        self.name=name;
        self.age=age;
        self.gender=gender;
    def get_name(self):
        return self.name;
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def eat(self):
        print("as a person,I can eat")
#这里使用构造方法构建一个Person实例。
jim=Person("jim","23","male");
print(jim.get_name(),jim.get_age(),jim.get_gender());
##重写普通方法和特殊的构造函数
##当一个类有一个父类或者多个父类，我们需要复写父类的方法时候，子类创建与父类同名的方法，
##同样构造方法也是这样。
class Man:
    def __init__(self,body,face,dick):
        self.body=body;
        self.face=face;
        self.dick=dick;
    def eat(self):
         print("as a man I can eat")
man=Man("nice","handsome","big");
##如果子类没有覆写父类的方法，然后去调用 会报错这个类没有eat这个成员方法
man.eat()
##调用超类的构造函数
class Woman(Person):
    def __init__(self,face,name,age,gender):
        Person.__init__(self,name,age,gender);
        self.face=face;
    def get_face(self):
        return self.face;
    def eat(self):
        print(self.get_name(),"like eate")

lyf=Woman("beauty","luoyufeng","25","female")
lyf.eat();
##使用函数super super如果使用的话就不用显式调用父类的init方法了 用super的话就不用传参self了
class Child(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
    def intro_myself(self):
        print(self.name,self.age,self.gender)
loli=Child("lolita","13","female")
loli.intro_myself();
##元素访问
##这个不搞了 就是手动实现下序列的一些基本方法
##从list,dict,str中派生
class Custom_sequence(list):
     def __init__(self,*args):
         super().__init__(*args);
         self.counter=0;
     #重写get_intem
     def __getitem__(self, index):
         self.counter+=1;
         return super(Custom_sequence,self).__getitem__(index)
cl=Custom_sequence(range(10));
print(cl)
cl.reverse()
print(cl)
##特性 存取方法；通过setget存取方法定义的属性通常称为属性 property

##函数 property
class Rctangle:
    def __init__(self):
        self.width="0";
        self.length="0";
    def set_size(self,size):
        self.width,self.length=size
    def get_size(self):
        return self.width,self.length;
    size=property(get_size,set_size)
##相当于把属性组合成为一个tuple了通过调用函数property并将存取方法作为参数（获取方法在前，设置方法在后）
r=Rctangle();
r.width="10";
r.length="19";
print(r.size)
##静态方法和类方法
##静态方法和类方法是这样创建的，将他们分别包装在
##staticmethodhe classmethod中，静态方法中没有self 可以直接通过类来调用
##类方法的定义中包含类似与self的参数，通常被命名 为cls
##类方法可以通过实例来调用也可以通过类来调用

class Myclass:
    ##定义静态方法
    def eat():
        print("i like eate")
    eat=staticmethod(eat)
    ##定义类方法
    def class_method(cls):
        print("this is a class method")
    class_method=classmethod(class_method)

Myclass.eat()
Myclass.class_method()
##getattr 与 setattr

class Custom_class:
  def __init__(self):
      self.width=0;
      self.length=0;
  def __setattr__(self, key, value):
      if key=="size":
          self.width,self.length=value;
      else:
          self.__dict__[key]=value
  def __getattr__(self, name):
      if name=="size":
          return self.width,self.length;
##__getattr__
##在访问name值的属性的时候，如果没有 那么会调用__getattr__这个方法来处理
##如果有改name值名称的属性，那么直接返回该属性的值
## set同样道理
###迭代器__iter__

class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self;
fibs=Fibs();
for f in fibs:
    if f>1000:
        print(f)
        break;
###生成器 包含yield语句的函数都被成为生成器
nested=[[1,2],[3,4],[5]]
##一个二维数组
def flatten(nested):
    for sublist in nested:
        for element in  sublist:
            yield  element
print(list(flatten(nested)))
##递归生成器
def  flatten_2(nested):
    for sublist in  nested:
        for element in flatten(sublist):
                yield  element

print(list(flatten_2(nested)))