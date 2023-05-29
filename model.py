# Purpose: Contains the model for the DFA
# author: ajwlforver
# version: 0.1
# date: 2023-05-29


# alpahbet: set of symbols
# Q: set of states
# q0: initial state  (q0 in Q)  
# F: set of final states (F in Q)
# delta: transition function (Q x alpahbet -> Q)

class dfa():
    def __init__(self,alpahbet, Q, q0, F, delta) -> None:
        self.alpahbet = alpahbet
        self.Q = Q
        self.q0 = q0
        self.F = F
        self.delta = delta

    def __str__(self) -> str:
        return "nil"
    
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
    

    def is_valid(self):
        # check if the DFA is valid
        # check if the alpahbet is valid
        # check if the Q is valid
        # check if the q0 is valid
        # check if the F is valid
        # check if the delta is valid
        return True
    
    