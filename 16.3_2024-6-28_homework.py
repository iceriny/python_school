# 今天写个简单的游戏吧!
# 这次的作业我会先写出来，然后跟着做一遍~


import random


# 定义角色类，用于创建游戏中的角色
class Character:
    count = 0  # 类变量，用于记录所有角色的数量

    def __init__(self, name: str):
        """
        初始化角色的基本属性
        :param name: 角色的名字
        """
        self.id = Character.count  # 角色的唯一标识
        Character.count += 1  # 更新角色数量
        self.name = name
        self.type = None  # 角色类型，默认为None
        self.hp = 100  # 角色的生命值，默认为100
        self.attack_power = 10  # 角色的攻击力，默认为10
        self.defense = random.randint(0, 5)  # 角色的防御力，随机生成0-5之间的值
        self.xp = 10  # 角色的经验值，默认为10

    def attack(self, target: "Character"):
        """
        角色攻击目标
        :param target: 被攻击的角色
        """
        damage = max(
            random.randint(0, 5), self.attack_power - target.defense
        )  # 计算伤害值 伤害公式为: max(随机生成0-5之间的值, 角色的攻击力 - 目标角色的防御力)
        target.hp -= damage  # 对目标造成伤害
        print(f"{self.name}攻击了{target.name} 造成了{damage}点伤害!")

    def __str__(self) -> str:
        """
        返回角色的字符串表示，用于显示角色的名字和生命值
        """
        return f"{self.name} : {self.hp}"

    def judge_death(self):
        """
        判断角色是否死亡
        :return: 如果角色生命值小于等于0，返回True；否则返回False
        """
        if self.hp <= 0:
            print(f"{self.name}死亡!")
            return True
        else:
            return False


# 定义敌人类，继承自角色类
class Enemy(Character):
    def __init__(self, name: str):
        """
        初始化敌人的属性
        :param name: 敌人的名字
        """
        super().__init__(name)
        self.type = "enemy"  # 敌人的类型设置为"enemy"


# 定义玩家类，继承自角色类
class Player(Character):
    def __init__(self, name: str):
        """
        初始化玩家的属性
        :param name: 玩家的名字
        """
        super().__init__(name)
        self.type = "player"  # 玩家的类型设置为"player"
        self.attack_power = 20  # 玩家的攻击力设置为20
        self.level = 1  # 玩家的等级，默认为1
        self.max_hp = 100  # 玩家的最大生命值，默认为100

    def up_level(self):
        """
        玩家升级，提升属性
        """
        self.attack_power += 5  # 攻击力增加5
        self.defense += 5  # 防御力增加5
        self.hp = self.max_hp  # 生命值恢复到最大值
        self.level += 1  # 等级增加1
        self.xp = 0  # 经验值重置为0
        print(f"{self.name}升级了!")


# 敌人生成工厂类，用于创建和管理敌人
class EnemyFactory:
    def __init__(self):
        """
        初始化敌人生存列表
        """
        self.current_enemy = []

    def judge_enemy_is_null(self):
        """
        判断当前是否有敌人存在
        :return: 如果敌人列表为空，返回True；否则返回False
        """
        if len(self.current_enemy) == 0:
            return True
        else:
            return False

    def get_random_name(self):
        """
        随机生成敌人的名字
        :return: 随机选择的敌人名字
        """
        name = random.choice(["史莱姆", "哥布林", "牛头人", "兽人", "翼人"])
        return name

    def create_enemy(self, level: int):
        """
        根据玩家的等级创建相应数量的敌人
        :param level: 玩家的等级
        """
        for i in range(level):
            self.current_enemy.append(
                Enemy(self.get_random_name())
            )  # 创建敌人并添加到敌人列表

    def remove_enemy(self, id: int):
        """
        移除指定ID的敌人
        :param id: 敌人的ID
        """
        self.current_enemy = [enemy for enemy in self.current_enemy if enemy.id != id]

    def __str__(self) -> str:
        """
        返回敌人生存列表的字符串表示，用于显示敌人的信息
        """
        result = f"当前敌人: \n"
        for enemy in self.current_enemy:
            result += f"{enemy}\n"
        result += "\n"
        return f"当前敌人数量: {len(self.current_enemy)}\n" + result


# 游戏类，包含游戏的主要逻辑
class Game:
    """
    游戏类的初始化方法，创建玩家对象和敌人生存工厂
    """

    def __init__(self):
        """
        初始化游戏，创建玩家和敌人生存工厂
        """
        self.player = Player("player")  # 创建玩家角色，使用默认名称`player`
        self.enemy_factory = EnemyFactory()  # 创建敌人生存工厂

    def start(self):
        """
        开始游戏，进行战斗直到玩家死亡或退出游戏
        """
        print("欢迎来到游戏世界!")
        print("进行多场战斗，当玩家血量小于等于0时游戏结束!")
        player_name = input("请输入你的名字: ")
        if player_name != "":  # 如果玩家输入了名字，则使用输入的名字作为玩家名字
            self.player.name = player_name  # 设置玩家名字

        is_continue = True  # 是否继续游戏 控制游戏的循环是否继续
        self.main_loop(is_continue)
        print(f"=====\n你一共杀死了{Character.count - 1}个敌人!\n=====")

    def main_loop(self, is_continue):
        """
        游戏的主循环，负责游戏流程的驱动
        """
        while is_continue:
            print("===================")
            print("1. 继续游戏")
            print("2. 退出游戏")
            choice = input("请选择: ")
            print("-------------------")
            # 根据选择执行不同的操作
            if choice == "1" or choice == "":
                print(self.player)  # 显示玩家信息
                if self.enemy_factory.judge_enemy_is_null():
                    self.enemy_factory.create_enemy(
                        self.player.level
                    )  # 根据玩家等级创建敌人
                print(self.enemy_factory)  # 显示当前敌人信息
                # 遍历当前场景中的所有敌人
                for enemy in self.enemy_factory.current_enemy:
                    # 玩家攻击敌人
                    self.player.attack(enemy)
                    # 检查敌人是否被击败
                    if enemy.judge_death():
                        # 从敌人列表中移除击败的敌人
                        self.enemy_factory.remove_enemy(enemy.id)
                        # 玩家获得经验
                        self.player.xp += 10
                        # 检查玩家是否达到升级条件
                        if self.player.xp >= 40:
                            # 玩家升级
                            self.player.up_level()

                # 遍历当前场景中的所有敌人，进行反击
                for enemy in self.enemy_factory.current_enemy:
                    # 敌人攻击玩家
                    enemy.attack(self.player)
                    # 检查玩家是否死亡
                    if self.player.judge_death():
                        # 如果玩家死亡，游戏继续的标志设为False
                        is_continue = False
                # 打印敌人工厂的状态，用于调试或展示
                print(self.enemy_factory)
            # 如果用户选择退出游戏
            if choice == "2":
                # 输出游戏结束信息
                print("游戏结束!")
                # 游戏继续的标志设为False，结束游戏循环
                is_continue = False


if __name__ == "__main__":
    game = Game()
    game.start()
    input(
        "按任意键退出"
    )  # 使用input函数等待用户输入，防止如果在控制台中运行程序时，程序突然退出导致的不自然


# 来试着做一个游戏吧，参考上面的例子，最好是做出点不一样的东西哦~
