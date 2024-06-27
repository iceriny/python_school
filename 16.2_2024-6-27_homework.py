"""
来做一个投骰子的游戏吧~

要求:
使用面向对象的思维
定义一个叫`Dice`的类 它具有 `size` 的属性 和一个 `roll()` 方法 分别表示其面数 和 投掷动作
定义一个 `DiceAction` 的类 它具有 `dices` 的属性 和一个 `roll()` 方法
其中`dices`属性是一个字典，字典的键为投掷的骰子，值为投掷的次数
`roll()` 方法将会投掷所有的骰子，将其结果存储在`self.result`中，例如:
'''
本次投掷共投掷了3个4面骰子、2个6面骰子、1个20面骰子，其结果如下:
d4: 2, 4, 1
d6: 5, 3
d20: 17
'''
当打印`DiceAction`实例时，将返回以上信息(`self.result`)
如果打印实例时，还未进行投掷，则抛出`ValueError`异常

测试以上功能，并符合预期输出

"""

import random


class Dice:
    def __init__(self, size: int) -> None:
        self.size = size

    def roll(self) -> int:
        return int(random.random() * self.size) + 1


class DiceAction:

    def __init__(self, dices: dict[Dice, int]) -> None:
        for dice, num in dices.items():
            if not isinstance(dice, Dice):
                raise TypeError("dice must be Dice")
            if not isinstance(num, int):
                raise TypeError("num must be int")
            if num < 0:
                raise ValueError("num must be positive")
            self.dices = dices

            self.result = {}

    def roll(self):
        # 重置结果字典，防止与上次结果冲突
        self.result.clear()
        for dice, num in self.dices.items():
            self.result[f"d{dice.size}"] = []
            for i in range(num):
                self.result[f"d{dice.size}"].append(dice.roll())

    def __str__(self) -> str:
        result = "本次投掷共投掷了"
        dices = []
        if not self.result:
            raise ValueError("该骰子还未进行投掷")
        for r in self.result.keys():
            dices.append(r)
        result += "、".join(dices) + "，其结果如下:\n"
        for r in self.result.keys():
            result += f"{r}:" + ", ".join(map(str, self.result[r])) + "\n"
        return result


# test:

d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)
d100 = Dice(100)


dice_action1 = DiceAction({d4: 3, d6: 2, d20: 1})

# 测试`未进行投掷`时抛出的异常
try:
    print(dice_action1)
except ValueError as e:
    print(e)


dice_action1.roll()
print(dice_action1)

dice_action2 = DiceAction({d4: 2, d6: 5, d20: 3})
dice_action2.roll()
print(dice_action2)
