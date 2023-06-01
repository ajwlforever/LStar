#  核心方法
#  L*算法的核心方法是成员查询（membership query）与等价查询(equivalence query), 通过这两个方法来构造DFA
# author: 虞启贤
# date: 2023-06-01
# version: 0.1
#
#
 
from models.dfa import DFA


# OT Table
# S: 字母表Σ表示下的前缀闭合的字符串集合。预示当前学习程度中可能的状态。
# E: 字母表Σ表示下的后缀闭合的字符串集合。E可以用来区分S状态。
# S中元素s和E中元素e组成的字符串t = s·e，表示要向SUT查询的一个字符串。
# S1：S·Σ 表示状态的转移。 Σ 表示字母表。
# transition: 为映射函数，T = (S∪S·Σ)×E -> {0,1}
class OTTable():
    def __init__(self, S: set, E: set, S1: set, transition : dict) -> None: # type: ignore
        self.S = S
        self.E = E
        self.S1 = S1
        self.transition = transition
        self.DFA = None
        pass 
    def __init__(self) -> None:
        pass

    #
    def add_prefix(self, s):
        self.S.add(s)
    def add_suffix(self, e):
        self.E.add(e)
        
# 成员查询: 是一个完善OT表中transition的过程
def membership_query():
    return None


#等价查询
def equivalence_query():
    return None

