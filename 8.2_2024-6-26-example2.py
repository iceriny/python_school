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
有了之前的方法，我们基本实现了所需要的功能
但是我们可以让我们的方法更加灵活一点
来吧，直接编写代码，跟着注释走~
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
# 之前的方法只能一次添加一个人的记录，现在我们想要更加灵活
# 一次添加多个人，并且可以添加多个记录
# 我们发现 之前的代码中，所以添加的数据结构都是一定的
# 那我们抽象出来一个方法，让这个方法生成一个这样结构的数据
# 换句话说，生成一个不绑定对应读者的单条记录
def create_record(book_name, borrow_date, return_status=False):
    return {
        "book_name": book_name,
        "borrow_date": borrow_date,
        "return_status": return_status,
    }


# 这样我们可以通过传入不同的参数批量生成记录


# 现在我们利用上面的新方法，结合之前例题时候实现的方法
# 稍加改造，实现`添加一个人 单次的借阅记录`
def add_record(reader_name, book_name, borrow_date, return_status):
    # 首先判断这个读者有没有历史借阅记录
    if reader_name in Borrowing_Record:
        # 如果有，那么就在这个读者的借阅记录中添加新的记录
        Borrowing_Record[reader_name].append(
            create_record(
                book_name, borrow_date, return_status
            )  # 调用刚刚抽象出来的方法
        )
        return True  # 返回True表示这是个老读者，有历史记录
    else:
        # 如果没有，那么就创建这个读者的借阅记录
        Borrowing_Record[reader_name] = [
            create_record(book_name, borrow_date, return_status)
            # 调用刚刚抽象出来的方法 对吧，把一致的功能抽象出来就可以多次调用
            # 这样就可以省去很多功夫，所以函数的很重要的一个意义就是 `代码复用`
        ]
        return False  # 返回False表示这是个新读者，没有历史记录


# 好哦，现在我们再次实现了`添加一个人 单次的借阅记录`
# 那我们就可以一次添加一个人的多条记录了
def add_records(reader_name, *records):
    records = [create_record(**record) for record in records]
    # 上面一句话其实信息量很大，这也是python的厉害之处
    # 我们来拆解一下
    # 首先，这是一个列表推导式
    # `*records` 是一个元组，元组中的每个元素都是一个字典
    # 遍历它!
    # 获取到字典`record`
    # 我们可以通过**来解包这个字典，然后通过关键字参数的形式传入到`create_record`方法中
    # 还记得么, 这个方法返回一个单条记录
    # 这样就可以生成一个以单条记录为元素的列表
    # 然后我们通过extend来添加到Borrowing_Record中
    # 这样就可以实现一次添加一个人的多条记录了
    if reader_name in Borrowing_Record:
        # 如果有，那么就在这个读者的借阅记录中添加新的记录
        Borrowing_Record[reader_name].extend(records)
        return True  # 返回True表示这是个老读者，有历史记录
    else:
        # 如果没有，那么就创建这个读者的借阅记录
        Borrowing_Record[reader_name] = records
        return False  # 返回False表示这是个新读者，没有历史记录


# 如果上面理解了，那要终极挑战了!
# 我们需要一个方法，实现添加多个人的多条记录
# 我们可以利用之前实现的方法，再加一层循环
def add_records_for_multiple_people(*multiplayer_records):
    # 这是一个不定数参数对吧
    # 实际上`multiplayer_records`就是一个元组 它代表多人的多条记录
    # 现在我们遍历它!
    for single_records in multiplayer_records:
        # 现在的`single_records`就是单人的多条记录了
        # 它也是一个元组，第一个元素是读者姓名
        # 第二个元素是记录
        # 总之 我们把它传入到我们上面的添加单人的多条记录的方法中
        add_records(single_records[0], *single_records[1])


# 那么我们可以有查找记录的方法
def find_record(reader_name):
    """
    根据读者名称查找借阅记录。

    参数:
    reader_name (str): 读者的姓名。

    返回:
    list or None: 如果找到读者的借阅记录，返回该记录列表；否则返回None。
    """
    if reader_name in Borrowing_Record:  # 如果找到，返回该记录列表
        return Borrowing_Record[reader_name]
    else:
        return None  # 如果没有找到，返回None


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
    if records is None:  # 如果没有找到，返回None
        return None
    else:  # 如果找到，遍历记录，筛选未归还的记录
        unreturned_records = []  # 创建一个空列表用于存储未归还的记录
        # 遍历借阅记录，筛选未归还的记录
        for record in records:
            if (
                record["return_status"] == False
            ):  # 如果归还状态为False，则添加到未归还记录列表中
                unreturned_records.append(record)
        return unreturned_records  # 返回未归还的记录列表


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
    if unreturned_records is None:  # 如果没有找到，返回None
        return None
    else:  # 如果找到，返回最近一次未归还的记录
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
    if reader_name in Borrowing_Record:  # 如果找到，返回该记录列表的最后一个
        return Borrowing_Record[reader_name][-1]
    else:
        return None


# 测试!

# 添加多条记录
add_records_for_multiple_people(
    ( # 这一层是第一个人的元组
        "susu", # 名字
        ( # 多条记录
            {"book_name": "book1", "borrow_date": "2023-06-23", "return_status": True},
            {"book_name": "book2", "borrow_date": "2023-06-24", "return_status": True},
            {"book_name": "book3", "borrow_date": "2023-06-25", "return_status": False},
        ),
    ),
    (# 第二个人的元组
        "lulu", # 名字
        ( # 多条记录
            {"book_name": "book4", "borrow_date": "2023-06-23", "return_status": False},
            {"book_name": "book5", "borrow_date": "2023-06-24", "return_status": True},
            {"book_name": "book6", "borrow_date": "2023-06-25", "return_status": False},
        ),
    ),
)

# 查找!
print("查找susu的全部记录")
print(find_record("susu"))

# 获取未归还的记录
print("查找susu的未归还的记录")
print(get_unreturned_records("susu"))

# 获取最近一次未归还的记录
print("查找susu的最近一次未归还的记录")
print(get_latest_unreturned_record("susu"))

# 获取最近一次借阅记录 不管是否归还
print("查找susu的最近一次借阅记录 不管是否归还")
print(get_latest_record("susu"))

print("查找lulu的最近一次借阅记录 不管是否归还")
print(get_latest_record("lulu"))
