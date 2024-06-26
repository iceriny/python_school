"""
这次的作业还是用 `蒙特卡洛方法` 计算圆周率

但这次不一样的是我们需要用类来写

要求:
定义一个基类`Shape`，
定义`Shape`的子类，`Point`， `Circle`  和  `Rectangle`
让shape具有`位置(position)`的属性
`Point`具有`x`和`y`的属性 和一个类方法: 通过传入一个`Rectangle`实例，返回一个随机点(Point)
`Circle`具有`半径(radius)`的属性 和一个判断一个点是否在圆内的方法
`Rectangle`具有`宽度(width)`和`高度(height)`的属性

使用这些类和其方法计算圆周率


提示:
1. 类方法通过在方法前加上`@classmethod`装饰器来实现
例如:
class A:
    @classmethod
    def method(cls):
        pass

2. 如果在某个类定义前，需要用到类型注释，可以使用字符串来表示类型注释
例如:
class A:
    def method(self, a: "B") -> "C":
        pass
class B:
    pass
class C:
    pass

"""

import math
import random


class Shape:
    def __init__(self, *position: float):
        self.x, self.y = position


class Point(Shape):

    @classmethod
    def get_random_point(cls, range: "Rectangle"):
        # 生成矩形宽度和高度范围内的随机偏移量
        random_x = range.left_2.x + random.uniform(0, range.width)
        random_y = range.left_2.y + random.uniform(0, range.height)
        return cls(random_x, random_y)


class Circle(Shape):

    def __init__(self, radius: float, *position: float):
        super().__init__(*position)
        self.radius = radius

    def inside(self, point: Point):
        # 计算点到圆心的距离 距离公式是: sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distance = math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
        # 判断距离是否小于半径
        if distance <= self.radius:
            return True  # 点在圆内
        else:
            return False  # 点在圆外


class Rectangle(Shape):

    def __init__(self, width: float, height: float, *position: float):
        super().__init__(*position)
        self.width = width
        self.height = height
        self.left_1 = Point(self.x - self.width / 2, self.y + self.height / 2)
        self.left_2 = Point(self.x - self.width / 2, self.y - self.height / 2)
        self.right_1 = Point(self.x + self.width / 2, self.y + self.height / 2)
        self.right_2 = Point(self.x + self.width / 2, self.y - self.height / 2)


# test:
# python中，约定 常数 全部大写
RADIUS = 5  # 半径
POSITION = (0, 0)  # 位置
RANDOM_COUNT = 100000  # 随机点总数量

# 创建圆和矩形
circle = Circle(RADIUS, *POSITION)
# 创建一个圆的外切正方形
rectangle = Rectangle(circle.radius * 2, circle.radius * 2, circle.x, circle.y)

# 初始化在圆内的随机点的数量
inside_count = 0
for i in range(RANDOM_COUNT):
    # 生成随机点
    p = Point.get_random_point(rectangle)

    # 判断点是否在圆内
    if circle.inside(p):
        inside_count += 1

# 计算π值
pi = inside_count / RANDOM_COUNT * 4
print(pi)
