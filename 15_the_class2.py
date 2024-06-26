# 通过之前的小作业
# 你应该感觉出来，好像不太对
# 如果是不同种类的动物，它们的叫声是不一样的
# 所以我必须要创建一个属性来储存它的叫声内容
# 但是这不合理
# 因为动物除了会叫之外，它们还有各种不一样的行为
# 也就是说，不同种类的动物有不同的方法才行啊
# 如果我们把每一种动物都创建一个类
# 那倒是功能实现了
# 但是我们发现，它们有很多重复的代码
# 毕竟都作为`动物`，它们有很多类似的特征
# 所以，我们希望把一些动物都相同的特征提取出来
class Animal:
    count = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Animal.count += 1

    def look(self, target):
        print(f"{self.name}正在看{target.name}")

    def speak(self):
        pass


# 好了，我们把它们共有的特征(属性)提取抽象出来，作为一个父类`Animal`
# 那怎么才能让不同的动物都具备上面的特征呢?
# 这就是`类的继承`
class Dog(Animal):
    count = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Dog.count += 1

    def speak(self):
        print("汪汪汪!")

    def run(self):
        print(f"{self.name}在跑!")


class Cat(Animal):
    count = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Cat.count += 1

    def speak(self):
        print("喵喵喵!")

    def jump(self):
        print(f"{self.name}在跳!")


class Bird(Animal):
    count = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Bird.count += 1

    def speak(self):
        print("叽叽喳喳!")

    def fly(self):
        print(f"{self.name}在飞!")


# 我们通过在类名的后面加上一个括号，里面放上父类的名字
# 这样，我们就实现了`继承`，子类就具备了父类的所有属性和方法
# 我们只需要在子类中，再添加一些自己特有的属性和方法即可
# 这样，我们就实现了`多态`，不同的动物，有不同的叫声
# 注意，我在构造函数中的第一行，使用`super()`方法调用父类的构造函数
# 这样，子类就具有了父类的属性
# 下面创建若干个实例来看看吧

dog = Dog("旺财", 2, "男")
dog2 = Dog("憨憨", 3, "男")
cat = Cat("招财猫", 1, "女")
bird = Bird("小黄鸡", 1, "男")

dog.speak()
cat.speak()
bird.speak()


dog.run()
dog2.run()
cat.jump()
bird.fly()

dog.look(cat)
bird.look(dog)

print("动物数量:", Animal.count)
print("狗狗数量:", Dog.count)
print("猫猫数量:", Cat.count)
print("小鸟数量:", Bird.count)


# 需要额外了解的是
# 类可以继承自多个父类
# 当继承多个父类时
# 父类中的同名方法，会按照从左到右的顺序进行覆盖
