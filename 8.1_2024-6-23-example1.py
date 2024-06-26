# 这是一个例题

"""
题目:
假设你正在帮助一个图书馆管理系统开发一个功能模块，该模块需要处理图书馆读者的借阅记录，借阅记录包括以下数据：

读者姓名（str）
图书标题（str）
借阅日期（str，格式为"YYYY-MM-DD"）
返还状态（bool，True表示已还，False表示未还）
"""

"""
思考:
处理借阅记录，那么首先我需要储存记录
用什么方式储存比较好呢?
列表? 不太好，要是有很多借阅记录，我要获取到对应的记录会需要遍历整个列表，效率会比较低
有没有什么可以快速定位到对应记录的容器呢?
字典? key是读者姓名，value是借阅记录
啊，没问题。
还有一个问题，上面的value是借阅记录，但是借阅记录又包含读者姓名，图书标题，借阅日期，返还状态
那么，借阅记录应该如何储存呢?
还用字典么?
好像是没问题，但是我们分析一下就会发现
如果使用字典，我们第一个要明确的就是
什么是key，什么是value
作为记录，其中的读者姓名，图书标题，借阅日期，返还状态，都可能重复，都不适合作为key
况且，一个人的借阅记录不会有特别多，这时候如果遍历，好像也不会很慢
再然后，借阅记录是有先后顺序的，所以，这很适合用一个列表来表示
所以我们得到这样的结论
整个存储的数据是一个字典
字典的key是读者姓名
value是这个读者的借阅记录
借阅记录是一个列表
列表的元素是另一个字典
这个字典中包含表示读者姓名，图书标题，借阅日期，返还状态的字段(成员)

然后需要考虑的是
我们有了这样的数据结构
作为管理模块
一定要可以添加和查找借阅记录
所以一定有
添加 和 查找 这样的方法(函数)
下面开始编写代码
"""

# 首先 定义一个作为模板的数据结构，这样后面编写方法时候更清晰


Borrowing_Record = {
    "Lolo": [
        {
            "book_name": "Python从入门到放弃",
            "borrow_date": "2023-06-23",
            "return_status": False,
        }
    ]
}
# 上面的数据结构是模板，当编写完代码可以把里面的内容删除掉


# 现在开始实现添加记录的方法
def add_record(reader_name, book_name, borrow_date, return_status):
    # 首先判断这个读者有没有历史借阅记录
    if reader_name in Borrowing_Record:
        # 如果有，那么就在这个读者的借阅记录中添加新的记录
        Borrowing_Record[reader_name].append(
            {
                "book_name": book_name,
                "borrow_date": borrow_date,
                "return_status": return_status,
            }
        )
        return True # 返回True表示这是个老读者，有历史记录
    else:
        # 如果没有，那么就创建这个读者的借阅记录
        Borrowing_Record[reader_name] = [
            {
                "book_name": book_name,
                "borrow_date": borrow_date,
                "return_status": return_status,
            }
        ]
        return False # 返回False表示这是个新读者，没有历史记录

# 那么我们可以有查找记录的方法
def find_record(reader_name):
    """
    根据读者名称查找借阅记录。

    参数:
    reader_name (str): 读者的姓名。

    返回:
    list or None: 如果找到读者的借阅记录，返回该记录列表；否则返回None。
    """
    if reader_name in Borrowing_Record: # 如果找到，返回该记录列表
        return Borrowing_Record[reader_name]
    else:
        return None # 如果没有找到，返回None

def get_unreturned_records(reader_name):
    """
    获取指定读者未归还的借阅记录。

    参数:
    reader_name (str): 读者的姓名。

    返回:
    list or None: 如果读者没有借阅记录或所有借阅记录均已归还，则返回None；否则返回未归还的借阅记录列表。
    """
    # 查找指定读者的借阅记录
    records = find_record(reader_name)
    if records is None: # 如果没有找到，返回None
        return None
    else: # 如果找到，遍历记录，筛选未归还的记录
        unreturned_records = [] # 创建一个空列表用于存储未归还的记录
        # 遍历借阅记录，筛选未归还的记录
        for record in records:
            if record["return_status"] == False: # 如果归还状态为False，则添加到未归还记录列表中
                unreturned_records.append(record)
        return unreturned_records # 返回未归还的记录列表

# 基础功能完成了 我们就可以添加一些拓展的功能
# 比如获取最近一次未归还的记录
def get_latest_unreturned_record(reader_name):
    """
    获取指定读者最近一次未归还的借阅记录。

    参数:
    reader_name (str): 读者的姓名。

    返回:
    dict or None: 如果读者没有借阅记录或所有借阅记录均已归还，则返回None；否则返回最近一次未归还的借阅记录。
    """
    # 获取指定读者的未归还的借阅记录
    unreturned_records = get_unreturned_records(reader_name)
    if unreturned_records is None: # 如果没有找到，返回None
        return None
    else: # 如果找到，返回最近一次未归还的记录
        return unreturned_records[-1]

# 比如获取最近一次借阅记录 不管是否归还
def get_latest_record(reader_name):
    """
    获取指定读者最近一次的借阅记录。
    参数:
    reader_name (str): 读者的姓名。
    返回:
    dict or None: 如果读者没有借阅记录，则返回None；否则返回最近一次的借阅记录。
    """
    if reader_name in Borrowing_Record: # 如果找到，返回该记录列表的最后一个
        return Borrowing_Record[reader_name][-1]
    else:
        return None


# 好了 现在测试一下吧

# 添加记录
add_record("Susu", "Python从入门到放弃", "2023-06-23", False)
add_record("Susu", "Java从入门到放弃", "2023-06-23", True)

# 查找记录
print(find_record("Susu"))

# 获取最近一次未归还的记录
print(get_latest_unreturned_record("Susu"))

# 获取最近一次借阅记录 不管是否归还
print(get_latest_record("Susu"))