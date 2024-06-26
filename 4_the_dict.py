# 什么是字典呢
# 字典顾名思义，我们可以结合现实中的字典来理解
# 现实中我们查字典，就是先从目录找到要查询的东西
# 然后通过目录给出的索引找出具体的内容
# 编程中的字典也类似
# 就是有一个`索引`然后每个索引对应一个特定的内容
# 比如:
child = {"name": "小明", "age": 18, "sex": "男"}
# 空字典的创建可以用{}来创建
empty_dict = {}
# 上面定义的名叫`child`的字典
# 索引是name, age, sex
# 每个索引对应一个特定的内容
# 比如name对应小明, age对应18, sex对应男
# 我们可以通过索引来获取对应的内容
print(child["name"])
# 前面的索引我们给它起个名叫`键`(key)
# 后面的内容我们起名叫`值`(value)
# 一个以`键`和`值`组成的成对结构称`键值对`(key-value pair) 或者叫(item)
print("-------分割线-------")

# python中的字典可以理解为一个可变的键值对集合
# 每个键值对以`,`分割，键值对的关系以`:`表示
# 作为`键`，必须是`唯一的`，一本字典里不能有两个`第1页`对叭?
# 但是`值`是可以重复的
child = {"name": "小明", "age": 18, "sex": "男", "height": 180, "weight": 180}
# 小明是大胖子，他的身高和体重都是180，emmmm...总之，值是可以重复的~

# 修改字典里的内容就相对列表很容易了
# 毕竟你可以通过索引来获取对应的内容
child["name"] = "小红"
child["age"] = 16
child["sex"] = "女"
child["height"] = 168
child["weight"] = 52
# 改完之后再打印看看
print(child)
# 输出结果如下:
# {'name': '小红', 'age': 16, 'sex': '女', 'height': 168, 'weight': 52}
# 添加键值对也很简单
child["address"] = "北京"
# 删除键值对也很简单
del child["weight"]
# 删除键值对之后再打印看看
print(child)
# 输出结果如下:
# {'name': '小红', 'age': 16, 'sex': '女', 'height': 168, 'address': '北京'}


print("-------分割线-------")
# 值可以是任何对象，你能想到的任何东西，我们之前学的列表，元组，字符串，等等
# 但是键不行
# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
# 假如你这么做了，那就会报错啦~
# 比如:
# tinydict = {['Name']: 'Runoob', 'Age': 7}
# print ("tinydict['Name']: ", tinydict['Name'])
# 你可以把上面的代码取消注释运行一下试试，VSCode的取消注释按键是`Ctrl+/`
# 选中对应的内容按下`Ctrl+/`即可

print("-------分割线-------")
# 字典当然有大小~
print(len(child))

# 字典的内置方法:
print("-------分割线-------")
print(child.keys()) # 返回成员是全部键的列表
print(child.values()) # 返回成员全部值的列表
print(child.items()) # 返回以 `元组` 组成的列表，元组的第一个元素是键，第二个元素是值
print("-------分割线-------")

# 复制
child_copy = child.copy()
print(child_copy)

print("-------分割线-------")
# get函数
# (注意这里我使用了python的多行写法，不用特意记忆，慢慢就会的)
print(
    "这是一个get函数的用法，第一个参数是键，第二个参数是键不存在时的默认值",
    child.get("name", "不存在"),
)
# setdefault函数
# 和`get()`类似, 但如果键不存在于字典中，将会添加键并将值设为default
print(
    "这是一个setdefault函数的用法，第一个参数是键，第二个参数是键不存在时的默认值",
    child.setdefault("name", "不存在"),
)

print("-------分割线-------")
# 当然可以进行成员判断
print("判断键是否存在", "name" in child)

print("-------分割线-------")
# 把字典dict2的键/值对更新到dict里.
child.update({"QQ": "123456"})
print("update() ①", child)
# 更新-->意为可以更改本来就存在的值
child.update({"age": "18", "height": "172"}) # 小红长大了~
print("update() ②", child)

print("-------分割线-------")
# 取出字典 key（键）所对应的值。
# 取出意为: 找到那个键值对，然后删除掉那个键值对，然后再返回这个键值对的值。
# 如果 key 不存在，返回默认值。
address = child.pop("address", "不存在")
print("address", address)
print("pop()", child)

print("-------分割线-------")
# 取出最后一个键值对 (还是`取出`哦)
last_item = child.popitem()
print("popitem()", last_item)


print("-------分割线-------")
# 清空字典
child.clear()
print("clear()", child)
