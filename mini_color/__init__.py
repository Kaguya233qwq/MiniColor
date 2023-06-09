import random
from enum import IntEnum


class Style(IntEnum):
    """
    The enum class of styles and effects for printing text

    样式和效果类
    """
    """终端默认"""
    Default = 0

    """高亮显示"""
    HighLight = 1

    """下划线"""
    UnderLine = 4

    """闪烁"""
    Flash = 5

    """反白显示"""
    AntiWhite = 7

    """不可见"""
    Invisible = 8


class Color(IntEnum):
    """
    The class of colors for printing text

    颜色类
    """
    """无颜色"""
    NONE = 0

    """黑色"""
    BLACK = 30

    """红色"""
    RED = 31

    """绿色"""
    GREEN = 32

    """黄色"""
    YELLOW = 33

    """蓝色"""
    BLUE = 34

    """紫色"""
    PURPLE = 35

    """青色"""
    CYAN = 36

    """白色"""
    WHITE = 37

    @classmethod
    def random(cls):
        """
        Return a random color

        随机色
        """
        return random.choice(list(cls))
