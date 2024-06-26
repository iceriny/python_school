'''
在Python中，数据类型大致可以分为两种处理方式：
值类型（也称为不可变类型，如整数、浮点数、字符串、元组）和引用类型（也称作可变类型，如列表、字典、集合）。
值类型变量存储的是值的直接拷贝，当值类型变量被赋值给新的变量时，会创建这个值的一个副本；
而引用类型变量存储的是值的内存地址，当引用类型变量被赋值给新的变量时，实际上是创建了一个指向原内存地址的新引用。
相当于告诉变量去什么地方找到数据。

下面通过一个例子来展示这两种类型的区别：
'''

### 值类型（不可变类型）示例：整数

# 整数是值类型
a = 10
b = a

# 修改b的值，a的值不受影响
b = b + 5

print("a的值是:", a)  # 输出：a的值是: 10
print("b的值是:", b)  # 输出：b的值是: 15


### 引用类型（可变类型）示例：列表

# 列表是引用类型
list1 = [1, 2, 3]
list2 = list1

# 修改list2，由于list1和list2指向同一片内存区域，所以list1也会受到影响
list2.append(4)

print("list1的内容是:", list1)  # 输出：list1的内容是: [1, 2, 3, 4]
print("list2的内容是:", list2)  # 输出：list2的内容是: [1, 2, 3, 4]

# 看吧，上面两个例子
# 明明都是把第二个变量赋值给第一个变量
# 为什么在列表的例子中修改了list2，list1的值也跟着变了
# 但在数字的例子中却是修改了b的值，a的值不受影响。

### 解释
'''
- 在整数的例子中，
尽管我们让 `b` 持有了 `a` 的值，
但当给 `b` 赋予一个新值时，
实际上是创建了 `5` 与 `a` 值的和的一个新副本，
然后让 `b` 指向这个新值，而 `a` 依然指向原来的值，
因此它们的值互不影响。

- 对于列表的例子，
`list1` 被赋值给 `list2` 时，
实际上是 `list2` 获取了 `list1` 所指向的内存地址。
因此，当修改 `list2` 时，由于它们指向同一片内存，
原列表（通过 `list1` 访问）也会显示相同的修改。
'''