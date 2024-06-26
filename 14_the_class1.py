# 类(Class)是一个抽象的概念
# 它表示某`一种`具有同样特指的`对象`
# 或者说，是某一种对象的`蓝图`或`模板`
# 它包含这种对象的`属性(Attribute)`表示其某些特征
# 以及`方法(Method)`表示其`行为`
# 一个类其实就是这些属性和方法的结合体

# 比如:
# 下面我们定义一个叫`人类(Human)`的类
"""
class Human:
    pass
"""
# 上面就是Human类的定义
# 这个类没有具体实现，我们会使用`__init__`函数来让这个类具有一定的属性
"""
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
"""


# 现在类具有了一些属性，它具有`名字``年龄`和`性别`
# 这是一个`人类`所具有的属性
# 我们把`人类`这个概念给抽象出来，定义出的class`Human`
# 人类可以说话对吧
# 所以我们还可以给`人`这个类增加一个方法`speak`，表示它具有说话的行为
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, words):
        print(self.name, "说:", words)


# 记得么，类是一个模板，是蓝图，是指代的`某一种`概念
# 所以，类的定义并不会特指这种概念的某个实体
# 作为`Human`类，我们可以通过这个模板来创建出来多个`实体`
# 这些实体，在`面向对象`编程中，被称为`实例`或者叫为`对象`
# 比如:
lolo = Human("Lolo", 18, "女")
susu = Human("Susu", 20, "女")

# python中的实例，是通过`类名(参数)`来构造的
# 在创建实例的过程中，其实是自动调用了类中的`__init__`方法
# 所以`__init__`方法叫做类的`构造函数`
# 现在我们可以让上面两个实体说话了
lolo.speak("你好呀")
susu.speak("下午好~洛洛!")

# 你可能注意到，上面的定义类里面的方法时，其第一个参数都是`self`
# 这个`self`其实指代的是这个实例本身
# 我们想想，当我们定义`类`的时候，是在写模板对吧
# 这时候我们想在方法中有一个东西可以指代将来实例化出来的`对象(实例)`
# 这就是`self`这个特殊参数的作用
# 在`__init__`方法中的属性的定义是`self.属性名`
# 就是意思是，这是`实例的属性`，所以这种`self.属性名`的属性，我们叫`实例属性`
# 默认情况下，我们可以可以通过`.`这个成员访问符号，来访问或者修改这些属性
print(lolo.name)
print(susu.name)
lolo.name = "洛洛"
susu.name = "酥酥"
print(lolo.name)
print(susu.name)

# 需要明确一个概念，当我说`类(class)`时候，指的是上面的模板
# 而说类的实例的时候则是指的通过模板创建出来的实体
# 这是两个概念
# 所以当我说`类属性``类方法`和`实例属性``实例方法`也是两个概念
# 上面我们知道，`实例属性`和`实例方法`怎么定义
# 那什么叫做`类属性``类方法`
# 对于`人类`这个类，它可以具有`类属性`，比如`总人数` 我们给它起个名叫`total_number`的属性
# 它表示`人类`这个类的实例总数
# 为了不冲突，我们重新定义一个类`People`，本质上，我们重新定义`People`和上面的`Human`是两个类
# 但是为了演示，它只是换了个名字而已，还是指代`人类`这个概念


class People:
    total_number: int = 0

    def __init__(self, name: str, age: int, gender: str, secret: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.__secret = secret
        People.total_number += 1

    def __str__(self) -> str:
        return f"一个人类，名字叫{self.name}，年龄是{self.age}，性别是{self.gender}"

    def __think(self, words: str):
        return f"我在想{words}"

    def speak_secret(self):
        print(self.__secret)

    def speak(self, words: str, is_think: bool = False):
        if is_think:
            words = self.__think(words)
        print(self.name, "说:", words)


# 我们定义了一个类属性`total_number`，表示人类实例的总数
# 我们可以通过类名来访问这个属性
print(People.total_number)

lolo = People("Lolo", 18, "女", "我的银行卡密码是12345678")
susu = People("Susu", 20, "女", "我的钱包里一分钱也没有了")
# 在创建出来两个实例之后再打印出来
print(People.total_number)
# 我们在类的构造函数中，对`total_number`进行了`+1`的操作
# 所以每次创建实例之后，`total_number`都会加1
# 于是对于`total_number`的`值`，总是等于实例总数

# 你可能注意到，其中有一个实例属性的名字前有`__`两个下划线
# 这种属性被称为`私有属性`
# 私有属性不能被外部访问，但是可以被内部访问
# 比如:
# print(lolo.__secret)
# 上面这行代码取消注释运行后，将会报错，告诉你没有`__secret`属性
# 但是它可以在内部访问到
# 我们还定义了一个方法`speak_secret`，表示实例个体，自己把秘密说了出来
lolo.speak_secret()
susu.speak_secret()
# 同样的，如果一个方法被加上了`__`，那么他就是私有方法
# 私有方法不能被外部访问，但是可以被内部访问
# 比如:
# print(lolo.__think("我今天要打羽毛球"))
# 但可以被内部访问，比如你可能注意到
# 在`speak`方法中，有一个判断语句，如果`is_think`为`True`，那么就调用`__think`方法
lolo.speak("今天我要打羽毛球", True)

# 需要注意的是，实例可以访问类属性，但是类不能访问实例属性
# 比如:
print(People.total_number)
print(lolo.total_number)
print(susu.total_number)
# 你甚至发现，都没有办法写出来通过类访问实例属性的语句

# 下面来个小作业~
"""
定义一个类，表示动物
它具有属性：名字，年龄，性别，种类, 叫声内容(比如狗狗的话是"汪汪") 这五个属性
它具有方法：
    1. 叫(call)，用print函数模拟其叫声

实例化出若干个动物，并让它们叫出声
"""
