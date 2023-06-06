# Purpose: Contains the model for the DFA
# author: 虞启贤
# version: 0.1
# date: 2023-05-29


# alpahbet: set of symbols  ['a','b']
# Q: set of states   ['A','B']
# q0: initial state  (q0 in Q)  'A'
# F: set of final states (F in Q) ['B']
# delta: transition function (Q x alpahbet -> Q) 字典   {('A','a'):'B'}
 
# import Utils.PitureUtil

from typing import List


class DFA():
    def __init__(self,alpahbet : set, Q: List[str], q0 : str, F : List[str], delta: dict) -> None:
        self.alpahbet = alpahbet
        self.Q = Q
        self.q0 = q0
        self.F = F
        self.delta = delta
    
    ## 增加新的状态，符号，转换，终态，初态
    def add_state(self, q):
        # add a new state
        self.Q.append(q)
    def set_desp(self, desp):
        # set the description of the dfa
        self.desp = desp

    def add_alpahbet(self, a):
        # add a new symbol
        self.alpahbet.add(a)
    def add_transition(self, q, a, q_next):
        # add a new transition
        self.delta[(q,a)] = q_next
    def add_final_state(self, q):
        # add a new final state
        self.F.append(q)
    def add_initial_state(self, q):
        # add a new initial state
        self.q0 = q

    # 判断状态，action是否在dfa中
    def is_state(self, q):
        return q in self.Q
    def is_action(self, a):
        return a in self.alpahbet

    def __str__(self) -> str:
        return "nil"
    # 得到初态，终态，转换，符号，状态
    def get_q0(self):
        return self.q0
    def get_F(self):
        return self.F
    def get_delta(self):
        return self.delta
    def get_alpahbet(self):
        return self.alpahbet
    def get_Q(self):
        return self.Q
    def get_desp(self):
        return self.desp
    # 检查转换函数是否合法
    # 所有的边都在Q x alpahbet中, 所有的边的终点都在Q中 
    def is_valid_delta(self):
        if(len(self.delta) == 0):
            return False 
        for key in self.delta.keys():
            state = key[0]
            action = key[1]
            # 所有的边都在Q x alpahbet中
            if(state not in self.Q or action not in self.alpahbet): 
                print("state not in Q or action not in alpahbet")
                return False
            state2 = self.delta[key]
            # 所有的边的终点都在Q中
            if(state2 not in self.Q):
                print("%s not in Q" % state2)
                return False
             
        return True
        
    # 检查dfa是否有效
    # 首先检查所有状态，符号，初态，终态，转换函数是否合法
    def is_valid(self):
        # check if the DFA is valid
        # check if the alpahbet is valid
        # require: alpahbet is not empty
        if(len(self.alpahbet) == 0):
            print("alpahbet is empty")
            return False
        # check if the Q is valid
        # require: Q is not empty
        if(len(self.Q) == 0):
            print ("Q is empty")
            return False
        # check if the q0 is valid
        # require: q0 in Q and q0 is not empty
        if(self.q0 not in self.Q or self.q0 == None):
            print("q0 is empty or not in Q")
            return False
        # check if the F is valid
        # require: F is not empty and F is subset of Q
        if(len(self.F) == 0 or not set(self.F).issubset(set(self.Q))):
            print("F is empty or not subset of Q")
            return False
        # check if the delta is valid
        # require: delta is not empty and delta 的key是Q x alpahbet
        if(not self.is_valid_delta()):
            return False
        return True
    
    # show Image of DFA
    def show(self):
            return
    
    # 得到下一个状态
    def step(self, q, a): 
        # return the next state
        # 检查状态，action是否在dfa中
        if not(self.is_state(q) and self.is_action(a)):
            print("state %s or action %s is not in dfa" % (q,a) )
            return None
        # 检查是否有(q,a)这条边
        if (q,a) not in self.delta.keys():
            print("no edge (%s,%s)" % (q,a))
            return None
        return self.delta[(q,a)]
    
    # 运行dfa
    def run(self, s):
        # return the final state
        q = self.q0
        for a in s:
            q = self.step(q,a)
            # 如果没有(q,a)这条边，返回None
            if q == None:
                return None
        return q       
    
    # 检查dfa是否接受字符串
    def accept(self, s):
        # return if the string is accepted
        q = self.run(s)
        if q == None:
            return False
        return q in self.F
       


 