'''
# Part 1: 字符串操作

- 创建一个字符串 str1 = "Hello, World!"。
    - 打印出 str1 的长度。
    - 将 str1 中的所有字符转换为小写并打印。
    - 提取 str1 中从索引5开始到结束的子字符串并打印。
    - 使用字符串方法查找 "World" 在 str1 中的位置并打印。
    - 创建一个新的字符串 str2 = "Python"，将 str1 和 str2 连接在一起，并在它们之间插入一个空格，然后打印结果。
'''
# 1. 字符串操作
print('----------1. 字符串操作-----------')
str1 = "Hello, World!"
print(len(str1))  # 打印长度
print(str1.lower())  # 转换为小写
print(str1[5:])  # 提取子字符串
print(str1.find("World"))  # 查找子字符串位置
str2 = "Python"
print(str1 + " " + str2)  # 连接字符串
'''

# Part 2: 列表操作

- 定义一个列表 list1 = [1, 2, 3, 4, 5]。
    - 向 list1 的末尾添加数字6。
    - 从 list1 中移除数字3。
    - 查找数字4在 list1 中的索引位置并打印。
    - 将 list1 中的第二个元素（索引为1）替换为数字7。
    - 创建一个新列表 list2 = [6, 7, 8]，将 list1 和 list2 合并成一个新列表并打印。
'''
# 2. 列表操作
print('----------2. 列表操作-----------')
list1 = [1, 2, 3, 4, 5]
list1.append(6)  # 添加元素
list1.remove(3)  # 移除元素
print(list1.index(4))  # 打印索引位置
list1[1] = 7  # 替换元素
list2 = [6, 7, 8]
list1.extend(list2)  # 合并列表
print(list1)
'''
# Part 3: 综合

- 定义两个字符串 str1 = "apple,banana,grape" 和 str2 = "cherry,lemon,orange"，以及一个初始为空的列表 fruits_list。
    - 将 str1 和 str2 中的字符串通过逗号分隔，然后将分隔得到的每项元素分别添加到 fruits_list 中。
    - 创建一个新的字符串 result_str，其中包含 fruits_list 中所有元素，元素间以半角分号(;)分隔，并在每个元素前后各添加一个星号(*)作为装饰。
    - 找出 fruits_list 中出现的最长的字符串(如果有多个相等则输出第一个即可)，并将其打印出来。
'''
print('----------3. 综合-----------')
# 1. 字符串到列表的转换
str1 = "apple,banana,grape"
str2 = "cherry,lemon,orange"
fruits_list = str1.split(",") + str2.split(",")

# 2. 列表元素转换回字符串
result_str ="*".join(fruits_list)
print(result_str)
result_str = "*;*".join(result_str.split("*"))
# 这时候打印出来发现完成的字符串的两头没有`*`
print(result_str)
# 那我们给它加上!
result_str = "*" + result_str + "*"

# 3. 打印最长的字符串
max_len_fruit = max(fruits_list, key=len)
# 这里的key参数是一个函数，用来指定比较对象的长度，这里我们指定为len函数，即比较`fruits_list`的长度。
# 因为涉及到将函数作为参数传入到其他函数，所以最后这个其实是有点超纲的
print(max_len_fruit)

print(result_str)

'''
# 补充知识:
str的join方法:
字符串的 join() 方法的作用是将一个 iterable（可迭代对象，如列表、元组、集合等）中的元素连接起来，形成一个新的字符串。
在连接过程中， iterable 中的每个元素会被转换为字符串（如果还不是字符串的话），然后使用 join() 方法调用者（即指定的分隔符字符串）作为间隔符插入到这些字符串元素之间。
最终，所有元素被连接成一个单一的字符串。

例如，
如果你有一个字符串列表 ['Hello', 'world', '!']，
并且你使用 ' ' （一个空格）作为 join() 方法的参数，
它会返回字符串 'Hello world !'。
如果分隔符省略或为空，则元素之间不会有间隔，直接相连。

基本语法是：delimiter.join(iterable)
delimiter 是作为分隔符的字符串。
iterable 是要连接的元素序列，如列表、元组等。
注意，join() 是字符串对象的方法，因此你需要在某个字符串上调用它，并将要连接的 iterable 作为参数传递。
此外，iterable 中的所有元素在连接前都会被转换成字符串形式。

示例 1: 使用空格分隔字符串列表
"""
words = ["Hello", "world", "!"]
sentence = " ".join(words)
print(sentence)  # 输出: Hello world !
"""

示例 2: 使用逗号和空格分隔数字列表
"""
numbers = [1, 2, 3, 4, 5]
formatted_numbers = ", ".join(map(str, numbers))
print(formatted_numbers)  # 输出: 1, 2, 3, 4, 5
"""
在这个例子中，因为列表元素是整数，我们需要使用 map() 函数将它们转换为字符串，然后再使用 join()。

示例 3: 无分隔符连接字符列表
"""
chars = ['a', 'b', 'c', 'd']
concatenated_chars = ''.join(chars)
print(concatenated_chars)  # 输出: abcd
"""

示例 4: 使用特殊符号分隔混合类型列表
"""
mixed_items = ['Apple', 2024, 'Banana', True]
# 转换所有元素为字符串
as_strings = map(str, mixed_items)
separated_items = " | ".join(as_strings)
print(separated_items)  # 输出: Apple | 2024 | Banana | True
"""
这里，列表包含了不同类型的元素，通过先转换为字符串，再用特定分隔符连接。
'''