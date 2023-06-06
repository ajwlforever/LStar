## 测试core.py中的函数

import collections
import core
import pandas as pd
from models.sut import SUT
from Utils.PitureUtil import  render_to_pdf
from models.dfa import DFA

def test_transition():
    transition = {
        'a' : {
            'a' : 1,
            'b' : 0
        },
    }
     
   
    df = pd.DataFrame(transition)
    print(df)

# 创建一个只接受偶数个a或b的sut
def create_sut1():
    # 先创建这个dfa
    alpahbet = {'a','b'}
    Q = {'q0', 'q1', 'q2', 'q3'}
    q0 = 'q0'
    F = {'q0'}
    delta = {
        ('q0','a') : 'q1',
        ('q1','a') : 'q0',
        ('q1','b') : 'q2',
        ('q2','b') : 'q1',
        ('q2','a') : 'q3',
        ('q3','a') : 'q2',
        ('q3','b') : 'q0',
        ('q0','b') : 'q3'
    }
    dfa = DFA(set(alpahbet), Q, q0, F, delta)
    # render_to_pdf(dfa, "Img/test_sut")

    positive_samples = set()
    negative_samples = set()
    # 设定黑盒接受字符长度
    blackbox_accept_length = 10
    # 设定黑盒接受字符集合
    blackbox_accept_alphabet = {'a','b'}
    list1 = core.generate_all_strings(blackbox_accept_alphabet, blackbox_accept_length) 
    
    for s in list1:
        if dfa.accept(s):
            positive_samples.add(s)
        else:
            negative_samples.add(s)

    # print("positive_samples: ", sorted(positive_samples))
    # print("negative_samples: ", negative_samples)
    sut = SUT(positive_samples , negative_samples)
    return sut

def test_initialOTTable():
   positive_samples = {'a','b'}
   negative_samples = {'ab','ba','aa','bb'}
   sut = SUT(positive_samples , negative_samples)
   ot =  core.initial_otTable(sut, {'a','b'})
   print("初始化完成")
   ot.showTable()

def test_equivalence_query():
   
    sut =  create_sut1()
    ot =  core.initial_otTable(sut, {'a','b'})
    ot.showTable()
    ot = core.equivalence_query(sut, ot)
    ot.showTable()

#test_transition()
test_initialOTTable()

# create_sut1()
# test_equivalence_query()
