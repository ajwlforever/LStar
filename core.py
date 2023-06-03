#  核心方法
#  L*算法的核心方法是成员查询（membership query）与等价查询(equivalence query), 通过这两个方法来构造DFA
# author: 虞启贤
# date: 2023-06-01
# version: 0.1
#
#
 
import itertools
from models.dfa import DFA
from models.sut import SUT
import pandas as pd
# OT Table
# S: 字母表Σ表示下的前缀闭合的字符串集合。预示当前学习程度中可能的状态。
# E: 字母表Σ表示下的后缀闭合的字符串集合。E可以用来区分S状态。
# S中元素s和E中元素e组成的字符串t = s·e，表示要向SUT查询的一个字符串。
# S1：S·alphabet 表示状态的转移。 alphabet 表示字母表。
# transition: 为映射函数，T = (S∪S·Σ)×E -> {0,1}
class OTTable():
    # 映射函数用dict不利于更新和查询，
    def __init__(self, S: set, E: set, transition : dict, alphabet : set) -> None: 
        self.S = S
        self.E = E
        self.transition_S1 = dict()
        self.transition = transition
        self.alphabet = alphabet
        self.S1 = alphabet
        pass 
     
     
    def showTable(self): 

        print("S Length = ", len(self.S))
        df = pd.DataFrame(self.transition) 
        df1 = pd.DataFrame(self.transition_S1)
        print(df.T)
        print(df1.T)
        print(self.transition)
        return None
    
    #
    def add_prefix(self, s):
        self.S.add(s)
    def add_suffix(self, e):
        self.E.add(e)

    def del_epsilon(self, s : str) -> str:
        if s.startswith('ε'):
            s = s[1:]
        if s.endswith('ε'):
            s = s[:-1]
        return s
    
    # 更新映射函数，通过sut查询    
    def update_transition(self,sut : SUT):
        for s in self.S:
            for e in self.E:
                 
                res = sut.membership_query(s+e)
                
                self.transition.update(
                    {
                        s : {
                            e : res
                        }
                    }
                )
        for s in self.S1:
            for e in self.E:
                
                res = sut.membership_query(s+e)
            
                self.transition_S1.update(
                    {
                        s : {
                            e : res
                        }
                    }
                )
        return True

    # 检验闭合性一致性
    def check_property(self):
        self.closed = self.check_cloesed()
        self.consistent = self.check_consistent()
        return self.closed and self.consistent

    # 检验闭合性
    # 对于每一个t∈S⋅Σ，在S中都有一个对应的s使得row(s) = row(t)，我们称观察表（S,E,row）闭合。
    # 
    def check_cloesed(self):
        
        return True
    # 检验一致性
    def check_consistent(self):
        return False

# 成员查询: 是一个完善OT表中transition的过程
# 在目标黑盒系统进行对应查询，T(s,e) = 1 / 0.
# transition函数的值就是OT表中需通过membership query查询的每个entry，
# 每个entry就代表着learner向SUT查询过该对应string是否存在于正则语言L中。
# sut: 目标黑盒系统
# otTable: OT表
def membership_query(sut: SUT, otTable):
    otTable.update_transition(sut)
    return None

# 从Ot表中构造dfa
def construct_dfa(otTable):
    return None
 
    

#等价查询: 判断构造的dfa是否等价于黑盒系统
# 从OT表中构造DFA，然后从目标黑盒系统找到一个反例，将其添加到OT表中
def equivalence_query(sut: SUT, otTable):
    # 从OT表中构造DFA
    dfa = construct_dfa(otTable)
    # 从目标黑盒系统找到一个反例
    if  t := sut.get_counter(dfa) != None:
        # 将 t 及其所有前缀添加到OT表中 
        for i in range(len(t)):
            otTable.add_prefix(t[:i])
        #  使用Membership_query 扩展 transition 到 (S U S·Σ) × E 
        membership_query(sut, otTable)
        return None
    return dfa

def initial_otTable(sut: SUT, alphabet : set):
    # 一开始的S、E是空集
    S = {'ε'}
    E = {'ε'}
    transition = dict()
    oTTable = OTTable(S, E, transition ,alphabet)
    oTTable.update_transition(sut)
    return oTTable

# L*算法主要过程
# sut: 目标黑盒系统
def learn_dfa(sut, alphabet : set):
    
    ot = initial_otTable(sut, alphabet) # 初始化OT表 

    #重复这个过程 直到teacher认为sut == M
    while  True:
        while ot.check_property() == False:
            if ot.closed == False:
                #找 rows(S·Σ)⊆rows(S)
                # TODO
                
            
                #  使用Membership_query 扩展 transition 到 (S U S·Σ) × E 
                membership_query(sut, ot)
                pass
            if ot.consistent == False:
                # 其目的是为了保证S·Σ中每一项都在S中有属于同一个等价类的项#
                # 找一个，row(s1 a)   a∈Σ, s1∈S , 不同于row(s) s∈S
                # 添加 s1 a 到 S
                #TODO

                # 使用Membership_query 扩展 transition 到 (S U S·Σ) × E
                membership_query(sut, ot)

        # 当ot表满足闭合性和一致性时，将ot转换成自动机 M 
        # 等价查询找反例 , tracher 认为sut == M 则推出循环
        if dfa := equivalence_query(sut, ot) == None:
            break
        
# 生成所有的字符串
def generate_all_strings(blackbox_accept_alphabet, blackbox_accept_length):
    # 生成所有的字符串
    # 生成所有的字符串
    all_strings = []
    for i in range(1, blackbox_accept_length+1):
        all_strings += list(map(''.join, itertools.product(blackbox_accept_alphabet, repeat=i)))
    return all_strings