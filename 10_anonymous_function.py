# 作为参数的函数

# python有一个重要的概念
# 万物皆是对象
# 什么是对象，等到说面相对象的时候我们再详细讲解
# 暂时我们可以把`对象`理解为一个`物体(item)`
# 作为物体 具有属性和方法
# 比如 `笔` 这个物体，有长度、颜色等属性，有写、擦、喷墨等方法
# 我们不详细讲解具体的关于`对象`的概念
# 只是作为引申——函数，也是对象
# 是一种抽象的对象
# 实际上，函数的参数的传递，就是把不同的对象的控制权交给不同的`函数`来进行运算

# 我们来定义三个函数


def segmentation(msg):
    """将传入的字符串按空格分割，然后在空格处添加逗号并返回。"""
    result = msg.split(" ")
    return ", ".join(result)


def add_smile(msg):
    """在传入的字符串末尾添加一个笑脸并返回。"""
    return msg + " :)"


def string_handle(msg, *funcs):
    """将传入的字符串进行处理并返回。"""
    for func in funcs:
        msg = func(msg)
    return msg


# 现在我们有三个函数，前两个函数是实际的处理动作，第三个函数是真正的处理函数
# 我们在使用时，只调用第三个函数
# 传入要处理的字符串，和需要进行的处理动作
# 比如，如果我只想分割
print(string_handle("I love you", segmentation))
# 如果我只想添加笑脸
print(string_handle("I love you", add_smile))
# 如果我要同时分割和添加笑脸
print(string_handle("I love you", segmentation, add_smile))
# 以上的函数的使用，把函数本身作为参数传入到另一个函数中，这种接受函数作为参数的函数，称为`高阶函数`
# 而以这种形式为主要编程方式的，即
"""它将计算过程视为一系列函数的求值，
而不是像过程化编程那样侧重于执行指令序列或面向对象编程那样侧重于消息传递和对象状态。
在函数式编程中，函数被当作第一类公民对待，
这意味着函数可以被赋值给变量、作为参数传递给其他函数、从其他函数返回，
就像操作其他数据类型一样自然。"""
# 被称为 `函数式编程`
# 其实更加复杂，有`纯函数` `不可变数据` `递归` 等等的概念，在这里对于`函数式编程`只做了解即可

# 在上面的例子中，我们事先定义好了两个函数，作为处理的具体操作
# 如果在应用过程中
# 我们并没有预先定义好
# 并且使用频率不高(大多数情况仅一次)
# 那我们专门去给它定义一个函数就有些笨拙
# 有没有办法，定义一个`一次性的函数`?

# 匿名函数就是为了应对这样的需求而出现的
# 匿名函数在python中使用`lambda`关键字来定义
# 它有一定的限制
# 它可以具有任意数量的参数，但只能有一个表达式。
# 它的语法是: `lambda [arg1 [,arg2,.....argn]]: expression`
# 我们来看看具体的方法

# 现在我们有一个新的需求，要在输出的字符串的后面，添加一个`(灬ꈍ ꈍ灬)`
print(string_handle("I love you", lambda msg: msg + " (灬ꈍ ꈍ灬)"))
# 上面的语句，我们用`lambda`关键词引导定义了一个匿名函数，
# 函数的参数是`msg`，函数的具体逻辑是一个表达式: ` msg + " (灬ꈍ ꈍ灬)"`
# 我们在定义`string_handle`时候使用的是不定数参数对吧，所以我们可以传入多个匿名函数
print(
    string_handle(
        "I love you",
        lambda msg: msg + " (灬ꈍ ꈍ灬)",
        lambda msg: msg + f"[本字符串的长度是{len(msg)}]",
    )
)
# 当然，也可以传入之前定义好的函数，现在我们把全部的函数都放进去
print(
    string_handle(
        "I love you", segmentation, add_smile, lambda msg: msg + " (灬ꈍ ꈍ灬)"
    )
)


# lambda函数也可以有多个参数
# 但是我们在定义`string_handle`的时候，调用函数时使用的语句是`func(msg)`，也就是默认我们的匿名函数只有一个参数
# 所以如果要实际上定义一个接受任意参数数量函数作为参数的`高阶函数`，我们需要判断传入函数的参数数量，然后进行调用
# 这很麻烦，一般情况也是不建议这么写
# 所以我们只定义一个`高阶函数`，只接受一个函数作为参数
# 所以，我们重新修改下上面的函数
def pro_string_handle(func,**kwargs):
    msg = kwargs['msg']  # 获取`msg`关键字参数作为初始值
    msg = func(**kwargs)  # kwargs是传入的`关键字参数`记得么? 将`kwargs`解包传入到函数中
    return msg


# 现在我们就可以很方便的使用可以有任意个数参数的传入的参数函数了
# 将lambda函数的参数作为关键字参数传入到`pro_string_handle`中
print(
    pro_string_handle(
        lambda msg, number: msg * number, msg="[I love you]", number=2
    )
)
# 或者
print(
    pro_string_handle(
        lambda msg, string: msg + string, msg="I love you~ ", string="(✿◡‿◡)"
    )
)
