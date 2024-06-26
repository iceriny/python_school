'''
题目：

假设你有一个字典，其键是学生的姓名，值是一个列表，列表中包含学生的成绩（整数）。
另外，你还有一个集合，它包含了所有及格的学生的姓名（及格分数为60分）。

你的任务是：

遍历字典，打印出每个学生的姓名和他们的平均成绩（保留两位小数）。
遍历集合，对于集合中的每个学生，判断他们是否在所有科目中都及格（即每个成绩都大于等于60）。
如果是，打印出该学生的姓名和“All subjects passed!”。如果不是，打印出该学生的姓名和“Not all subjects passed.”。

tips:
保留两位小数的方法：
number = 3.1415926
number = round(number, 2)
或者使用字符串的格式化语法:
print(f"{number:.2f}")
'''

# 假设的输入数据如下：
students_scores = {
    'Alice': [85, 78, 92],
    'Bob': [58, 65, 72],
    'Charlie': [90, 90, 90],
    'David': [55, 75, 85],
    'Eve': [60, 60, 60]
}

passed_students = {'Alice', 'Bob', 'Eve'}

# 请根据以上内容，编写代码实现题目要求的功能:

# 答案代码：
for key, value in students_scores.items():
    print(f"{key}的平均成绩为{round(sum(value)/len(value), 2)}")


for name in passed_students:
    scores = students_scores.get(name, None)
    if scores is not None:
        # 遍历名叫name的学生的全部分数
        for score in scores:
            # 如果有一个分数小于60，则打印出该学生的姓名和“Not all subjects passed.”
            if score < 60:
                print(f"{name} not all subjects passed.")
                # 因为有一个分数小于60，所以后面的不用再判断啦，就跳出循环
                break
        else:
            # 如果循环结束，没有跳出循环，则说明所有分数都大于等于60，打印出该学生的姓名和“All subjects passed!.”
            print(f"{name} all subjects passed.")