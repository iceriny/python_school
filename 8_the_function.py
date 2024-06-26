# 什么是函数
# 函数就是一系列的语句的组合，用来完成一个功能的代码块
# 例如:


def print_hello():
    print("hello")


# 现在我们有一个函数叫`print_hello`
# 这是一个简单的函数，它只有一行语句，就是`print("hello")`
# 那为什么我们不在每次需要`print("hello")`时候都写出`print("hello")`
# 而是用函数呢?
# 假如我想要一个动态的字符串，让其中打招呼的对象可以不一样
# 如果我们每次都用print函数，那么我们每次都需要更改里面的字符串
# 非常的麻烦，所以，我们可以定义一个函数，然后调用这个函数


def print_hello_to(name):
    print("hello", name)


# 我们定义了一个函数，叫`print_hello_to`，这个函数接收一个参数`name`
# 这个函数的功能就是打印出`hello`和`name`，中间用空格隔开
# 我们可以调用这个函数，传入不同的参数，然后打印出不同的结果
print_hello_to("world")
print_hello_to("python")
print_hello_to("Lolo")

# 随后，作为初学者容易忽视的一点
# 函数的定义，并不执行函数中的代码
# 函数中的代码只有在调用时才会执行

print("-------分割线-------")


# 现在我们学会了怎么定义函数
# 那每次打印分割线那么麻烦
# 我们可以定义一个函数，叫`print_line`，这个函数的功能就是打印出"-------分割线-------"
# def print_line():
#     print("-------分割线-------")
# 但是这虽然方便很多，但是还是不够灵活
# 我们可以自定义分割线的标题
def print_line(title):
    print(f"-------{title}-------")


# 我们可以调用这个函数，传入不同的参数，然后打印出不同的结果
print_line("分割线")
print_line("分割线2")
print_line("分割线3")

print_line("函数返回值")
# 函数可以有返回值
# 上面的函数只是执行一个`print`的操作
# 所以不需要返回值(其实其返回值是`None`)
# 我们可以定义一个函数
# 它的功能是返回一个字符串，其内容是"hello"和"name"，中间用空格隔开


def get_hello_to(name):
    return "hello " + name


# 我们定义了一个函数，叫`print_hello_to`，这个函数接收一个参数`name`
# 这个函数的功能就是返回一个字符串，其内容是"hello"和"name"，中间用空格隔开
# 我们可以调用这个函数，传入不同的参数，然后打印出不同的结果
string = get_hello_to("Lolo")  # 调用函数，其返回值会赋值给`string`
print(string)  # 打印出`string`的值


print_line("函数的参数")


# 上面我们已经会了如何根据传入的参数不同来灵活的实现函数内部的功能
# 但是在定义参数的时候
# 还有很多技巧
# 默认值:
def print_hello_to_has_default(name="world"):  # 默认值是"world"
    print("hello", name)


# 这时候调用如果不提供name的参数内容，函数会默认认为name="world"
print_hello_to_has_default()  # hello world
print_hello_to_has_default("python")  # hello python
print_hello_to_has_default("Lolo")  # hello Lolo
# 换句话说，如果一个参数，在定义函数时不提供默认值
# 那这个参数就是`必需参数`
# 如果在调用函数时不提供这个参数的内容
# 那么就会报错

print_line("函数的参数 关键字参数")
# 关键字参数:
# 我们可以通过关键字来传递参数
print_hello_to_has_default(name="python")


# 这在有多个默认参数时会很有用
# 例如
def hello(name="world", language="english"):
    if language == "english":
        print("hello", name)
    elif language == "chinese":
        print("你好", name)
    else:
        print("hello", name)


# 我们可以调用这个函数，传入不同的参数，然后打印出不同的结果
hello()  # hello world
hello(name="python")  # hello python
hello(name="Lolo", language="chinese")  # 你好 Lolo
hello(language="chinese", name="Lolo")  # 你好 Lolo
hello(language="chinese")  # 你好 world
hello(name="Lolo")  # hello Lolo
# 用关键字传递参数可以无视函数在定义时，参数的顺序
# 否则你只能按照定义时的顺序传递对应的参数

print_line("函数的返回值")
# 函数的返回值也可以是多个的
# 下面是一个嵌套的字典
# 就是说字典的键对应的值是另一个字典
books = {
    "python": {"name": "python从入门到放弃", "price": 100},
    "java": {"name": "java从入门到放弃", "price": 200},
    "c++": {"name": "c++从入门到放弃", "price": 300},
}


# 我们来定义一个函数，通过提供`语言`，来获取书名和价格
def get_book(language):
    return books[language]["name"], books[language]["price"]


# 这个函数有两个返回值，它其实是返回了一个元组
python_book = get_book("python")
print(python_book)
print(type(python_book))
# 元组可以用这样的形式来进行解包
name, price = get_book("python")
print(name)
print(price)

print_line("不定长参数")


# 假设你要处理一组内容，但是这个内容的个数不是固定的
# 你可能很容易想到使用一个列表把他们打包
# 然后把这个列表作为参数传递给函数
# 但python还提供了另外的方式
# 那就是不定长的参数
# 首先使用普通的参数，这时候我们传入了一个包含多个列表的列表
def flatten_list(list_of_lists):
    # result = []
    # for list_of_list in list_of_lists:
    #     for item in list_of_list:
    #         result.append(item)
    # return result
    # 上面可以，但是我们更简单的使用一个嵌套的推导式
    return [item for list_of_list in list_of_lists for item in list_of_list]


the_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(flatten_list(the_lists))  # >>> [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 没问题吧，现在我们使用不定长参数的方式定义函数
def flatten_list_use_unfixed(*list_of_lists):  # `*list_of_lists`表示不定长参数
    return [item for list_of_list in list_of_lists for item in list_of_list]


print(
    flatten_list_use_unfixed([1, 2, 3], [4, 5, 6], [7, 8, 9])
)  # 看，我们分别传入了3个列表作为参数

print_line("使用 不定的 关键字参数")


# 除了可以传入不定数量的列表，我们还可以传入不定数量的关键字参数
# 这种参数实际上是一个字典
def print_key_value(**kwargs):  # `**kwargs`表示不定长参数
    for key, value in kwargs.items():
        print(key, value)


print_key_value(name="Lolo", age=18, gender="female")
