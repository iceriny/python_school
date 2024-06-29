<!-- 生成目录 -->

目录:
[TOC]

---

# 模块（Module）和包（Package）

在 Python 中，"包"（package）和"模块"（module）是组织和重用代码的两种基本方式，它们对于构建复杂的应用程序至关重要。

> 这是一个`*.md`文件，也就是`Markdown`语法的轻量级标记文本格式，我们在最开始已经安装了在`VSCode`中查看`Markdown`的插件
> **你可以在 VSCode 中，右键本文的空白位置，点击`MPE:打开侧边预览`来查看格式化后，更清晰的 md 文档。还可以右键出现的预览界面中的空白位置，点击`Open in Browser`，来通过默认浏览器查看。也可以点击`Export`来导出为相应的格式。**

## 模块（Module）

**模块**是 Python 程序的基本组织单元，它是一个包含了 Python 定义和语句的文件，通常以`.py`作为扩展名，换句话说，一个`*.py`文件就是一个模块。模块可以包含函数、类、变量以及其他的 Python 对象。使用模块可以实现代码的复用，避免重复编写相同的代码，同时也能使代码更加条理清晰，易于维护。

例如，你可以创建一个名为`math_utils.py`的模块，其中包含一些数学相关的函数，如计算阶乘或求和等。其他 Python 脚本或模块可以通过导入这个模块来使用这些功能，而无需在每个地方都重新编写这些函数。

> 下面是写在`math_utils.py`**模块**(文件)的代码：

```python
# math_utils.py
def factorial(n):
    """Calculate the factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_list(lst):
    """Return the sum of all elements in a list."""
    return sum(lst)
```

> 在另一个模块(`other_script.py`)中使用这个模块：

```python
# other_script.py
import math_utils

print(math_utils.factorial(5))  # 输出: 120
print(math_utils.sum_of_list([1, 2, 3]))  # 输出: 6
```

在`other_script.py`中，我们使用`import`关键字导入了`math_utils`模块，并使用其中的函数。

## 包（Package）

-   **包**是一种将相关模块组织在一起的目录结构，它提供了一种更高级别的组织形式。包本质上是一个包含`__init__.py`文件（可以为空）的目录，这个特殊文件表明该目录应当被当作一个 Python 包来处理。包可以包含模块和其他子包(嵌套)，从而形成一个层次化的命名空间，有助于管理大型项目中的代码结构。

-   使用包，你可以根据功能或逻辑将相关的模块分组，使得代码库更加整洁，同时也便于外部用户理解和使用你的库或框架。

> 假设我们有一个名为`my_project`的项目，里面有两个功能相关的模块放在一个名为`utils`的包里：

```
my_project/
│
├── my_project/
│   ├── __init__.py
│   └── main.py
│
└── utils/
    ├── __init__.py
    ├── math_utils.py
    └── string_utils.py
```

> 在`my_project/main.py`中，你可以这样导入`utils`包下的模块：

```python
from utils.math_utils import factorial # 使用`utils`包下的`math_utils`模块
from utils.string_utils import reverse_string # 使用`utils`包下的`string_utils`模块

print(factorial(5))  # 使用math_utils模块的功能
print(reverse_string("Hello"))  # 使用string_utils模块的功能
```

-   注意看，当导入多层次的文件结构中的模块或包时，我们同样使用`.`作为成员访问符号。

总结来说，模块是单个文件，用于封装特定功能的代码；包则是一个包含`__init__.py`文件的目录，用于组织和管理相关的模块，提供一种结构化的方式来组织大型项目。

# 虚拟环境的使用

Python 提供了虚拟环境（Virtual Environment）的概念，它可以为每个项目创建独立的 Python 环境，避免不同项目之间的依赖冲突。

-   如果不使用虚拟环境，当我们安装第三方库的时候——
    1. 如果一个项目使用的是某个第三方库的`A`版本，而另一个项目使用的是`B`版本，那么这两个项目就会相互影响，导致不能同时共存。
    2. 我们安装第三方库时，将会把它安装在系统的 Python 环境中，而不是项目专用的环境中，而 Python 环境的默认第三方库的安装目录在系统的 Python 安装目录下，这会占用系统的磁盘空间。
       所以，我们需要使用虚拟环境来解决这个问题。
       用 VSCode 创建虚拟环境非常简单

## 通过 VSCode 创建虚拟环境

1. 通过 VSCode 打开项目文件夹。
    - 打开干净的 VSCode 窗口，选择`File`(文件)->`Open Folder`(打开文件夹)，选择你的项目文件夹。 或者——
    - 在系统文件管理器中，右键项目文件夹，点击`使用VSCode打开`。
2. 创建一个 Python 模块文件，即`*.py`文件。
3. 进入文件后，可以看到右下角的状态栏中显示的当前的 Python 环境。如果你跟着本教程走下来，我们安装的 python 版本应该是`3.11.9`，那么当前 Python 环境应该是`Python 3.11.9 64-bit`。
4. 点击这个位置，将会在 VSCode 的顶部显示一个下拉菜单，这里可以选择当前可以使用的 Python 环境，现在我们项目文件夹里没有 python 的虚拟环境，所以我们可以——
5. 点击`Create Virtual Environment`(创建虚拟环境)，选择`venv`，选择`Python 3.11.9 64-bit`，点击`Create`(创建)。
    - 如果这里出现了问题，大概率说明你的网络对`pypi`的访问出现了问题，可以选择国内镜像源，或者开启代理的全局模式再次尝试。
    - 国内镜像源通常使用`清华`或者`阿里`的镜像源，可以百度如何更换`Python pip 镜像源`。
6. 创建完成后，当前 Python 环境将变成`venv`，表示当前使用的是项目专用的 Python 环境。

# 内置的原生库和第三方库的使用

## 内置的原生库

Python 自身附带了一些常用的内置库，它们可以直接使用，不需要安装。
比如我们之前使用的`random`库，可以直接使用`import random`来使用其中的功能。

## 第三方库

Python 提供了丰富的第三方库，它们提供了许多功能，包括网络请求、数据处理、图形绘制、机器学习、数据库连接等。这些库可以通过 pip 安装，然后通过 import 语句来使用。
本质上，第三方库其实就是一个` Python 包`，所以当使用第三方库时候，你可以通过`import`语句来使用它们提供的功能。
本次我们使用一个叫`icecream`的第三方库来进行演示，它提供了一种简单的方式来打印调试信息。

### 安装第三方库

安装第三方库的方法十分简单，在保证对`pypi`的网络通讯的前提下，在终端使用`pip install <包名>`即可。
所以，在 VSCode 中，在保证启动了虚拟环境后，我们先显示出终端:

1. 打开`终端`(Ctrl+Shift+`)
2. 在终端中，输入`pip install icecream`即可安装`icecream`库。
   这时候因为我们使用了虚拟环境，所以安装的库只会安装到虚拟环境中，不会安装到系统环境中。
   等显示出`Successfully installed <...>`字样后，我们就可以使用`icecream`库了。

### 使用第三方库

创建出一个新的 python 模块，起名叫`icecream_test.py`，然后输入以下代码：

```python
# icecream_test.py
from icecream import ic # 从icecream包中导入ic函数
ic(1)
ic("hello")
ic([1, 2, 3])
ic({"a": 1, "b": 2})
```

> 运行`icecream_test.py`，查看输出效果。
> 你还可以查看`icecream`库的[文档](https://github.com/gruns/icecream)，了解它详细的使用方法。

# 实战练习

#### 实战 1

我们先来一个简单的例子:

-   创建一个简单的 Python 脚本，使用`random`库生成一个随机整数，然后使用`icecream`库打印调试信息。

##### 额外教程

我们来使用 `os` 库 和 `open()` 函数 来读取文件的内容

```python
import os


def read_file(file_path):
    """
    读取指定文件路径的文件内容。

    参数:
    file_path: 字符串，文件的路径。

    返回:
    文件的内容，类型为字符串。

    抛出:
    FileNotFoundError: 如果文件路径不存在，则抛出此异常。
    """
    # 检查文件路径是否存在，如果不存在则抛出 FileNotFoundError
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")

    # 以只读模式("r")打开文件，并指定编码为 UTF-8
    with open(file_path, "r", encoding="utf-8") as file:
        # 读取文件全部内容并赋值给 file_content
        file_content = file.read()

        # 返回文件内容
        return file_content


def write_file(file_path, content):
    """
    将指定内容写入到指定文件路径的文件中。

    参数:
    file_path: 字符串，文件的路径。
    content: 要写入文件的字符串内容。

    抛出:
    FileNotFoundError: 如果文件路径不存在，则抛出此异常。
    """
    # 检查文件路径是否存在，如果不存在则抛出 FileNotFoundError
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")
    # 以写入模式("w")打开文件，并指定编码为 utf-8
    with open(file_path, "w", encoding="utf-8") as file:
        # 将内容写入文件
        file.write(content)


if __name__ == "__main__":
    # 定义文件路径
    file_path = "test.txt"

    # 读取文件内容
    content = read_file(file_path)

    # 合并并更新文件内容
    # 读取文件内容，追加新内容，并写回文件
    content += content + "\n" + "This is a test."

    # 将更新后的内容写回文件
    write_file(file_path, content)


```

#### 实战 2

现在我们来一个看起来像回事的练习:
首先安装`openpyxl`库，>> `pip install openpyxl`

在 python 中，我们使用`openpyxl`库来读取和操作 Excel 文件。
首先我们来导入这个模块

```python
import openpyxl
```

如果你熟悉`Excle`
你应该知道，一个`Excle`文件，可以理解为一个工作簿
而工作簿是由若干的`sheet`(工作表)组成的
工作表里有着若干`row`(行)和若干`column`(列)
这些列和行是由一个一个的`cell`(单元格)组成的
openpyxl 库就是把这些概念一个个的抽象成了不同的 python 类

所以，我们首先需要创建一个工作簿对象

```python
# 使用`openpyxl`创建一个工作簿对象
workbook = openpyxl.Workbook()
```

工作簿始终至少包含一个工作表。
您可以使用以下 Workbook.active 属性获取它：

```python
active_sheet = workbook.active
```

即，活动工作表，可以理解为当前工作表

您可以使用下列 Workbook.create_sheet()方法创建新的工作表：

```python
# 在末尾插入(默认)
ws1 = workbook.create_sheet("Mysheet")
# or
# 在第一个位置插入
ws2 = workbook.create_sheet("Mysheet", 0)
# or
# 插入到倒数第二个位置
ws3 = workbook.create_sheet("Mysheet", -1)
```

工作表在创建时会自动命名。它们按顺序编号（Sheet、Sheet1、Sheet2、…）。你可以随时使用`Worksheet.title`属性更改此名称 ：

```python
ws1.title = "New Title"
```

给工作表命名后，您可以通过键来访问对应的工作表：

```python
new_title_sheet = workbook["New Title"]
print(new_title_sheet.title)
```

您可以使用`Workbook.sheetname`属性查看工作簿中所有工作表的名称

```python
print(workbook.sheetnames)
```

**这个第三方库非常强大，几乎可以通过编程的方法实现 Excel 的所有功能。
具体的其他功能可以查看其[文档](https://openpyxl.readthedocs.io/en/stable/tutorial.html)**

##### 练习:

1. 创建一个工作簿对象
2. 将其的工作表命名为 "Test1"
3. 在其中写入以下的数据
   | 姓名 | 年龄 | 性别 |
   | ---- | ---- | ---- |
   | 张三 | 18 | 男 |
   | 李四 | 20 | 女 |
   | 王五 | 22 | 男 |
4. 将其保存为 "test.xlsx"
5. 然后打开这个文件，查看里面的内容
6. 在查阅其中无误后，继续使用 openpyxl 库，修改`张三`的名字为`张三丰`

###### 答案

! 先不要看答案哦~ 如果实在不会了再来看!

```python
import openpyxl

# 1. 创建一个工作簿对象
workbook = openpyxl.Workbook()

# 2. 将其的工作表命名为 "Test1"
sheet = workbook.active
if sheet is None:
    raise ValueError("No active worksheet found.")
sheet.title = "Test1"

# 3. 在其中写入数据
headers = ["姓名", "年龄", "性别"]
data = [
    ["张三", 18, "男"],
    ["李四", 20, "女"],
    ["王五", 22, "男"],
]

for col_num, header in enumerate(headers, 1):
    sheet.cell(row=1, column=col_num).value = header

for row_num, row_data in enumerate(data, 2):
    for col_num, cell_value in enumerate(row_data, 1):
        sheet.cell(row=row_num, column=col_num).value = cell_value

# 4. 保存为 "test.xlsx"

workbook.save("test.xlsx")

input("请手动打开 test.xlsx 文件，查看内容无误后，按回车键继续...")

# 6. 使用 openpyxl 库，修改`张三`的名字为`张三丰`
current_row = 2
for row in sheet.iter_rows(
    min_row=current_row, values_only=True
):  # 从第二行开始，获取每一行的值
    if row[0] == "张三":
        sheet.cell(row=current_row, column=1).value = "张三丰"  # 修改第一列的值
        break
    current_row += 1

# 保存修改后的文件
workbook.save("test.xlsx")

```
