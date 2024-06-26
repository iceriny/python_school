# 上一小节我们说了类的继承和多态
# 来总结一下关于类的概念
"""
- 类使用`class`关键字进行定义
- 使用`类名()`这样的语法进行实例的构造
- 类的实例化其实是调用了类的`__init__`方法
- 类具有属性和方法，和实例属性和实例方法
- 通过`__`表示私有的属性或方法
- 在实例属性和方法中一般使用`self`特指当前实例
- 在定义类的时候，使用`class 类名(父类名)`这样的语法进行定义继承关系
- 如果子类和父类有同名方法，子类的方法将会覆盖父类的方法
- 如果想要调用父类的同名方法，可以使用`super().方法名`这样的方式
"""

# 之前我们有定义过`__init__`和`__str__`方法
# 它们分别表示初始化方法和打印对象的方法
# 这种用`__`包裹的方法，叫做`魔法方法`
# python中有很多这样的魔法方法
# 它们都有不同的，特殊的作用


# 我们来抽象定义出一个类`Book`
# 并且使用各种魔法方法来演示一下
class Book:
    """
    书籍类，用于表示书籍的基本信息和操作。

    Attributes:
        name (str): 书籍的名称。
        author (str): 书籍的作者。
        price (float): 书籍的价格。
        content (list): 书籍的内容，以列表形式存储。
    """

    def __init__(self, name, author, price):
        """
        初始化书籍对象。

        Args:
            name (str): 书籍的名称。
            author (str): 书籍的作者。
            price (float): 书籍的价格。
        """
        self.name = name
        self.author = author
        self.price = price
        self.content = []

    def __str__(self) -> str:
        """
        返回书籍的字符串表示，包含书名、作者和价格。

        Returns:
            str: 书籍的字符串表示。
        """
        return f"《{self.name}》作者：{self.author}，内容数: {len(self)}, 价格：{self.price}"

    def __len__(self) -> int:
        """
        返回书籍内容的长度。

        Returns:
            int: 书籍内容的元素数量。
        """
        return len(self.content)

    def __getitem__(self, index) -> str:
        """
        根据索引获取书籍内容中的元素。

        Args:
            index (int): 元素的索引。

        Returns:
            str: 索引对应的书籍内容元素。
        """
        return self.content[index]

    def __setitem__(self, index, content) -> None:
        """
        设置书籍内容中指定索引位置的元素。

        Args:
            index (int): 元素的索引。
            content (str): 要设置的新内容。
        """
        self.content[index] = content

    def __delitem__(self, index) -> None:
        """
        删除书籍内容中指定索引位置的元素。

        Args:
            index (int): 要删除元素的索引。
        """
        del self.content[index]

    def __iter__(self):
        """
        返回书籍内容的迭代器。

        Returns:
            iterator: 书籍内容的迭代器。
        """
        return iter(self.content)

    def __add__(self, other):
        """
        计算两本书籍价格的总和。

        Args:
            other (Book): 另一本书籍对象。

        Returns:
            float: 两本书籍价格的总和。
        """
        return self.price + other.price

    def __iadd__(self, other):
        """
        将本书籍的价格与另一本书籍的价格相加，用于链式操作。

        Args:
            other (Book): 另一本书籍对象。

        Returns:
            Book: 自身对象，价格已更新。
        """
        self.price += other.price
        return self

    def __eq__(self, other) -> bool:
        """
        比较两本书籍的价格是否相等。

        Args:
            other (Book): 另一本书籍对象。

        Returns:
            bool: 如果价格相等则返回True，否则返回False。
        """
        return self.price == other.price

    def __gt__(self, other) -> bool:
        """
        比较本书籍的价格是否大于另一本书籍的价格。

        Args:
            other (Book): 另一本书籍对象。

        Returns:
            bool: 如果价格大于则返回True，否则返回False。
        """
        return self.price > other.price

    def __ge__(self, other) -> bool:
        """
        比较本书籍的价格是否大于等于另一本书籍的价格。

        Args:
            other (Book): 另一本书籍对象。

        Returns:
            bool: 如果价格大于等于则返回True，否则返回False。
        """
        return self.price >= other.price

    def __lt__(self, other) -> bool:
        """
        比较本书籍的价格是否小于另一本书籍的价格。

        Args:
            other (Book): 另一本书籍对象。

        Returns:
            bool: 如果价格小于则返回True，否则返回False。
        """
        return self.price < other.price

    def __le__(self, other) -> bool:
        """
        比较本书籍的价格是否小于等于另一本书籍的价格。

        Args:
            other (Book): 另一本书籍对象。

        Returns:
            bool: 如果价格小于等于则返回True，否则返回False。
        """
        return self.price <= other.price

    def __ne__(self, other) -> bool:
        """
        比较两本书籍的价格是否不相等。

        Args:
            other (Book): 另一本书籍对象。

        Returns:
            bool: 如果价格不相等则返回True，否则返回False。
        """
        return self.price != other.price

    def __contains__(self, item) -> bool:
        """
        检查书籍内容中是否包含指定元素。

        Args:
            item (str): 要检查的元素。

        Returns:
            bool: 如果内容中包含元素则返回True，否则返回False。
        """
        return item in self.content


book1 = Book("Python编程：从入门到实践", "Eric Matthes", 39.99)
book2 = Book("算法图解", "Aditya Bhargava", 25.50)

# 添加内容到书籍
book1.content.extend(
    [
        "第1章 引言",
        "第2章 安装Python",
        "第3章 编写第一个程序",
        "第4章 变量、常量和数据类型",
    ]
)
book2.content.extend(["第1章 什么是算法", "第2章 如何描述算法", "第3章 算法的效率"])

print(book1)  # 输出书籍信息 __str__

print(len(book1))  # 输出书籍内容长度 __len__

print(book1[1])  # 获取内容中的一个元素  __getitem__
book1[1] = "修改后的第2章内容"  # 修改内容中的一个元素  __setitem__
print(book1[1])  # 再次输出查看修改结果

del book1[
    3
]  # 尝试删除不存在的索引会抛出错误，这里正确示范应先确认索引存在  __delitem__
print(book1)

for chapter in book2:  # __iter__
    print(chapter)  # 遍历并打印书籍内容

total_price = book1 + book2  # 计算两本书的总价 __add__
print(f"两本书的总价为：{total_price}")


book1 += book2  # 更新book1的价格为两本书价格之和  __iadd__
print(f"更新后，《{book1.name}》的价格为：{book1.price}")

print(book1 == book2)  # 比较价格是否相等  __eq__
print(book1 > book2)  # 比较book1价格是否大于book2 __gt__
print(book1 < book2)  # 比较book1价格是否小于book2 __lt__
print(book1 != book2)  # 比较价格是否不相等 __ne__

print("第1章 引言" in book1)  # 检查内容中是否包含特定章节 __contains__
