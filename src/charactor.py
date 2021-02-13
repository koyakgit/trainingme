"""
キャラクター管理モジュール
"""
import os
import random

PARAMS = [
    "HP         ",
    "MP         ",
    "力         ",
    "精神力     ",
    "魔力       ",
    "根性       ",
    "美しさ     ",
    "かっこよさ ",
    "愛嬌       ",
    "健康       ",
    "気品       ",
    "教養       ",
    "カリスマ性 ",
    "知性       ",
    "棋力       ",
    "素早さ     ",
    "器用さ     ",
    "意外性     ",
    "目の良さ   ",
    "耳の良さ   ",
    "鼻の良さ   ",
    "敏感さ     "
]


class Charactor:
    """
    キャラクターパラメータ
    """

    def __init__(self, name):
        self.name = name
        self.parameters = {}
        for param in PARAMS:
            self.set_parameter(param, random.randrange(100))

    def set_parameter(self, key, value):
        self.parameters[key] = value

    def get_parameter(self, key):
        return self.parameters[key]

    def get_status(self):
        status = []
        status.append(f"名前 : {self.name}")
        power = 0
        for param in PARAMS:
            status.append(f"{param} : {self.parameters[param]}")
            power += self.parameters[param]
        status.append("----------------------")
        status.append(f"戦闘力      : {power}")
        return os.linesep.join(status)


if __name__ == "__main__":
    c = Charactor("ほげ")

    print(c.get_status())
