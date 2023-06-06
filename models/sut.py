# 目标黑盒系统
# author: 虞启贤
# version: 0.1
# 黑盒系统的目标是：给定一个字符串，判断一个字符串是否被该目标系统接受.
# 这个sut是 定义了一个包含正样本和负样本的样本数据集合。

from models.dfa import DFA

class  SUT():
    def __init__(self,positive_samples: list, negative_samples : list) -> None:

        self.positive_samples = positive_samples
        self.negative_samples = negative_samples

        pass

    # membership query
    # 成员查询：输入一个字符串到sut，sut判断是否被接受
    def membership_query(self, x : str) -> bool:
        if x.startswith('ε'):
            x = x[1:]
        if x.endswith('ε'):
            x = x[:-1]
        if x == '':
            return 1  # 空字符串 --》 接受
        for sample in self.positive_samples:
            if sample == x:
                return 1
        return 0
    

    # 等价查询：输入一个DFA，判断sut是否等价于DFA 
    # 返回一个反例, 这个反例是dfa不接受，但是黑盒系统会接受的字符串
    def equaivalence_query(self, dfa : DFA) -> bool:
        for sample in self.positive_samples:
            if dfa.accept(sample):
                return sample
            return None
        
    # 返回dfa可接受的一个反例
    def get_counter(self, dfa: DFA):
        for sample in self.negative_samples:
            if dfa.accept(sample):
                return sample
            return None
    