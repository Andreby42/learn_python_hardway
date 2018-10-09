###python中的异常处理机制
#result=1/0
#print(result)
##上面的代码会出现算术异常
##那么使用raise来让事情沿着你的指定的轨道来报错
#result=1/0
#raise  Exception("算术异常")
## try except finally
try:
    result=1/0
except  Exception:
    print("算术异常")
except Exception:
    print("你好")
except Exception:
    print("异常")
finally:
    print("系统退出")
##可以多个except 并行，但是如果第一个exception是Exception的话那么底下的子异常类不会走
##
try:
    #请注意这里输入的字符串，需要进行类型转换
    a=input("请输入一个数字")
    a=int(a);
    result=2/a
except (ZeroDivisionError):
    print("算术异常")
else:
    print("一切正常")
finally:
    del  a
    print("系统退出")
##如果 异常可以忽略，只需要发出警告的话使用 warnings中的函数warn
from warnings import  warn
warn("hello warn",DeprecationWarning)
##异常对象，
##引发异常 使用raise来引发异常，将一个异常类或者异常实例作为参数
##自定义异常类 需要继承Exception父类
class CustomException(Exception):
    print("something is wrong with the function")
try:
    # 请注意这里输入的字符串，需要进行类型转换
    a = input("请输入一个数字")
    a = int(a);
    result = 2 / a
except (CustomException):
        pass
else:
    print("一切正常")
finally:
    del a
    print("系统退出")

## 捕获遗产使用try except  可以包含多个except 方便对不同的异常进行处理
##else子语句，可以在具体的except后面进行添加else语句，方便没有引发异常的时候的程序运行
##finally 为了确保代码块无论是否引发异常都将执行，可以使用 try/finally try/catch/finally
##异常和函数，在函数中引发异常的时候可以将异常传播到调用函数的地方,异常的传播，
def test():
    raise  Exception("somthing is wrong with this function")
def test_test():
    test();
def test_try():
    try:
        test()
    except:
        print("Exception handled")
test_test();
test_try()
##警告 类似于异常，但是只是个警告纸打印一条错误消息，他们是warning的子类
