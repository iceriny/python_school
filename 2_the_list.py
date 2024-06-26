# 我们学了字符串啦
# 前面提到过 字符串其实很像数组 也就是一个个单个的`字符`组成的一列字符的有序排列
# 那我们把单个的`字符`换成叫`元素` 或者叫 `成员` 的概念
# 这种 有序的 多个 `成员` 的组合，就叫做 `数组` 或者我们叫 `列表`(list)

# 现在我们声明和初始化一个列表
the_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 当然可以是字符串
the_list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# 在python中列表的成员可以是不同的类型
the_list4 = ["a", 1, 2.0, True] # 分别是 `字符串` `整数` `浮点数` 和 `布尔值`(布尔值就是`真`(True)或者`假`(False))

print("--------成员访问和切片分割线-------")
# 在前面 我们通过对字符串的索引 来获取到字符串中对应位置的字符
# 现在我们把字符换成了对应的`成员`了对吧
# 同样可以用相同的方式来获取到成员
第4个成员 = the_list1[3]
print(第4个成员)
# 当然 可以用负数进行倒序访问
倒数第4个成员 = the_list1[-4]
print(倒数第4个成员)
# 还包括了切片~
第一到第三个成员 = the_list1[0:3]
print(第一到第三个成员)

print("--------成员赋值分割线-------")
# 那现在问题来啦，如果一个字符串被初始化了 我怎么改变其中的成员呢?
# 很简单，直接用索引赋值即可
the_list1[0] = 100
print(the_list1) # >>> [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("--------增加成员分割线-------")
# 如果想增加成员呢?
the_list1.append(11)
print(the_list1) # >>> [100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print("--------删除成员分割线-------")
# 如果想删除成员呢?
the_list1.remove(11)
print(the_list1) # >>> [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 注意 remove 方法会删除第一个匹配的成员
# 换句话说 如果列表中有多个成员是相同的
# 那么 remove 方法只会删除第一个匹配的成员
# 这也意味着 list 中 是允许有多个相同的成员的
the_list1.append(11)
the_list1.append(11)
print(the_list1) # >>> [100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]
# append 方法会添加到列表的末尾
# 删除成员的方法还可以用`del`关键字
del the_list1[-2:] # 删除倒数2个成员 `-2:`表示倒数第二个成员到末尾 是切片的简化写法
print(the_list1)

print("--------合并列表分割线-------")
# 除了用`+`进行列表的合并(就像前面的字符串一样)，还可以用`*`进行列表的复制(字符串也可以哦)
this_list = the_list1 * 2
print(this_list) # >>> [100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 也同样有 `in` 和 `not in` 的成员操作符
print(100 in the_list1)

print("--------列表比较分割线-------")
# 字符串是可以进行比较的
# 但是需要引入`operator`模块
# 至于什么是 模块 我们到后面会说到
# 导入 operator 模块
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))


# 列表常用的方法：

print("--------常用方法分割线-------")
# 列表的成员数量
print(len(the_list1))

# 获取最大的成员
print(max(the_list1))
# 最小的
print(min(the_list1))
# 将可以转换为列表的对象转换为列表
print(list("abc"))


print("--------列表方法分割线-------")
# 添加对象
# 前面有说过哦 记得么 append 方法会添加到列表的末尾
the_list1.append(999)

print("计数列表中成员出现的次数")
print(the_list1.count(999))

print("删除列表中匹配的第一个成员")
the_list1.remove(999)
print(the_list1)

print("追加多个成员")
the_list2.extend(["k", "l", "m"])
print(the_list2)

print("获取到某个值第一次出现的位置(索引) 如果没有找到 则返回 -1")
print(the_list2.index("k"))

# 插入成员
the_list2.insert(0, "z")
print("插入成员\n",the_list2)


print("移除列表中的一个元素（默认最后一个元素），并且返回该元素的值")
var = the_list2.pop()
print(var)
print(the_list2)

print("翻转列表")
the_list2.reverse()
print(the_list2)

print("排序列表")
the_list2.sort()
print(the_list2)

print("复制列表")
list_copy = the_list2.copy()
print(the_list2)
print(list_copy)

print("清空列表")
the_list2.clear()