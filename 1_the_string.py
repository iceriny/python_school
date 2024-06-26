#! print() 函数不带参数的话会输出一个空行
print()
#! 但是我们使用print("--------分割线-------")来进行分割会更加直观
print("--------分割线-------")
# 字符串在python中一般使用`str`来代替
# str可以看做是一个个单个`字符`的数组
# 现在我们有一个字符串`string`
string = "hello world"
# 当然也可以使用 `string = 'hello world'`这种单引号的形式初始化

# 打印它~
print(string)  # >>> hello world
print("--------分割线-------")

# 既然是数组 那么它一定有长度
# len()函数可以获取一个`可迭代对象`的长度 比如`数组` `字典` 等 具体什么是数组和字典 后面会讲
# 所以`str` 也是一个可迭代对象(或者近似的看做为`数组`)
# 那么我们想要获取长度 我们就使用len()函数
print(len(string))  # >>> 11
print("--------分割线-------")

# 因为是个数组 所以我们就可以使用`索引`来获取到其中某个特定位置的字符
# VV获取第一个字符VV
print(string[0])  # >>> h
# VV获取最后一个字符VV
print(string[-1])  # >>> d
# 你也看到了 索引 可以是负数
# 它代表从后往前的索引 但是与正数不同的是 它没有`-0`这种概念 毕竟`-0`还是0嘛
print("--------分割线-------")

# 我们还可以使用切片来获取字符串的一部分
# 切片就是获取字符串的一部分
# 切片的格式是 `[start:end]` 其中`start`是包含的 `end`是不包含的
# 所以`[0:1]`表示获取第一个字符
# 所以`[0:2]`表示获取第一个和第二个字符
print(string[0:1])  # >>> h
print(string[0:2])  # >>> he
# 空格也是字符哦
print(string[3:8])  # >>> lo wo

print("--------分割线-------")
# 这样我们就可以拼接一些字符串啦
# 比如 我们先有另一个字符串是:
lolo = "Lolo"
# 我们利用之前的`string`字符串进行一下拼接:
new_string = (
    string[0:5] + " " + lolo
)  # 获取到前面字符串的前五个字符 >>> 然后拼接上空格 >>> 然后拼接上lolo
print(new_string)  # >>> hello Lolo

print("--------分割线-------")
print("--------分割线-------")
# 转移字符串
# 记得之前说的 如果有出现想要输出`hello "world"`的时候么
# 当时我们使用的是把外面的双引号换成单引号
# 但有更通用的方法 特别是出现多层嵌套的引号时会很常用
# 那就是使用`\`作为转移字符放在需要转义的字符前面
print("'Hello, world!'")  # 输出：'Hello, world!'

print("Hello, world!\nHow are you?")  # 输出：Hello, world!
#       How are you?

print("Hello, world!\tHow are you?")  # 输出：Hello, world!    How are you?

print("Hello,\b world!")  # 输出：Hello world!

print("Hello,\f world!")  # 输出：
# Hello,
#  world!

print("A 对应的 ASCII 值为：", ord("A"))  # 输出：A 对应的 ASCII 值为： 65

print("\x41 为 A 的 ASCII 代码")  # 输出：A 为 A 的 ASCII 代码

decimal_number = 42
binary_number = bin(decimal_number)  # 十进制转换为二进制
print("转换为二进制:", binary_number)  # 转换为二进制: 0b101010

octal_number = oct(decimal_number)  # 十进制转换为八进制
print("转换为八进制:", octal_number)  # 转换为八进制: 0o52

hexadecimal_number = hex(decimal_number)  # 十进制转换为十六进制
print("转换为十六进制:", hexadecimal_number)  # 转换为十六进制: 0x2a

print("--------分割线-------")
# 前面我们进行字符串拼接时使用了`+`作为拼接的符号
# 其实这是字符串的运算符
# `+` 拼接符号
print("Hello" + " " + "World")  # >>> Hello World
# `*` 重复符号
print("Hello" * 3)  # >>> HelloHelloHello
# `[]`` 索引或切片符号
print("Hello"[3])  # >>> l
print("Hello"[1:3])  # >>> el
# `in` 成员运算符
print("H" in "Hello")  # >> True
# `not in` `非`成员运算符
print("H" not in "Hello")  # >> False


print("--------分割线-------")
# 字符串格式化
name = "Lolo"
age = 25
print("My name is %s and I am %d years old." % (name, age))
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
# 关于使用`%s`和`%d`来格式化字符串 还有其他的格式化符号 具体参考`https://www.runoob.com/python3/python3-string.html`中的`Python 字符串格式化`部分


print("--------分割线-------")
# 多行字符串
multi_line_string = """
This is a multi-line string.
It can span multiple lines.
"""
print(multi_line_string)


print("--------分割线-------")
# 字符串方法
# 有很多哦，具体的还是去参考`https://www.runoob.com/python3/python3-string.html`中的`Python 的字符串内建函数`部分
# 举一些例子
lolo = "lolo".capitalize()  # 将字符串的第一个字符转换为大写
print(lolo)
lolo = lolo.lower()  # 转换字符串中所有大写字符为小写.
print(lolo)
lolo = lolo.split("o") # 将字符串拆分成列表
print(lolo)
# ... 等等