# 装饰器是python的一种特殊的语法，可以理解为函数的函数
# 但是和`高阶函数`并不相同，因为装饰器返回的是函数，而不是函数的返回值
# 装饰器允许在不修改原有函数代码的基础上，动态地增加或修改函数的功能，
# 装饰器本质上是一个接收函数作为输入并返回一个新的包装过后的函数的对象。


# 装饰器函数
def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        # 这里是在调用原始函数前添加的新功能
        ...

        result = original_function(*args, **kwargs)

        # 这里是在调用原始函数后添加的新功能
        ...

        return result

    return wrapper


# 使用装饰器
@decorator_function
def target_function(arg1, arg2):
    pass  # 原始函数的实现


# 上面展示了装饰器的结构和如何使用
# 我们来写个案例
# 我想让被装饰的函数在调用时，输出一个log信息
# 其中有当前的函数名，函数的参数，函数的返回值
def log_function(original_function):
    """
    创建一个装饰器，用于记录函数调用及其参数和返回值。

    参数:
    original_function: 被装饰的原始函数。

    返回:
    一个包装函数，它在调用原始函数前后打印出相关信息。
    """

    def wrapper(*args, **kwargs):
        """
        执行原始函数前后的日志记录。

        参数:
        *args: 原始函数的的位置参数。
        **kwargs: 原始函数的关键字参数。

        返回:
        原始函数的返回值。
        """
        # 在调用原始函数前，记录函数名及其接收到的参数
        print(
            f"Calling {original_function.__name__} with args: {args}, kwargs: {kwargs}"
        )
        # 调用原始函数，并存储其返回值
        result = original_function(*args, **kwargs)
        # 在调用原始函数后，记录函数的返回值
        print(f"{original_function.__name__}() returned: {result}")
        return result

    return wrapper


# 现在我们定义一个功能函数，但是在前面用上面的装饰器函数装饰
@log_function
def add(a, b):
    return a + b


# 来实验一下
add(1, 2)  # 注意我在使用`add`的时候没有`print`哦
# 输出以下结果
"""
Calling add with args: (1, 2), kwargs: {}
add returned: 3
"""


# 装饰器本质上是一个函数
# 那么它当然也可以有参数
# 我来定义一个装饰器函数，
# 让被装饰的函数在调用时在打印log信息的同时，输出传入的字符串
def log_function_with_message(message):
    """
    创建一个装饰器，用于记录函数调用及其参数和返回值，并附加自定义消息。

    参数:
    message: 要附加到日志中的消息。

    返回:
    一个包装函数，它在调用原始函数前后打印出相关信息，并附加自定义消息。
    """

    def decorator(original_function):
        """
        创建一个装饰器，用于记录函数调用及其参数和返回值，并附加自定义消息。
        参数:
        original_function: 被装饰的原始函数。
        返回:
        一个包装函数，它在调用原始函数前后打印出相关信息，并附加自定义消息。
        """

        def wrapper(*args, **kwargs):
            """
            执行原始函数前后的日志记录，并附加自定义消息。
            参数:
            *args: 原始函数的的位置参数。
            **kwargs: 原始函数的关键字参数。
            返回:
            原始函数的返回值。
            """
            # 在调用原始函数前，记录函数名及其接收到的参数
            # 在调用原始函数前，记录函数名及其接收到的参数
            print(f"Log Message: {message}")
            print(
                f"Calling {original_function.__name__} with args: {args}, kwargs: {kwargs}"
            )
            # 调用原始函数，并存储其返回值
            result = original_function(*args, **kwargs)
            # 在调用原始函数后，记录函数的返回值
            print(f"{original_function.__name__}() returned: {result}")
            return result

        return wrapper

    return decorator


@log_function_with_message("This is a custom message.")
def sub(a, b):
    return a - b


sub(20, 10)
# 输出以下结果
"""
Log Message: This is a custom message.
Calling sub with args: (20, 10), kwargs: {}
sub returned: 10
"""


## 除了函数，装饰器也可以是类，即`类装饰器`
# 因为还没有学到类(class)，这里制作了解
class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 在调用原始函数之前/之后执行的代码
        ...
        result = self.func(*args, **kwargs)
        # 在调用原始函数之后执行的代码
        ...
        return result

@DecoratorClass
def my_function():
    pass
