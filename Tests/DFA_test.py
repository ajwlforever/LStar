 
from  .models.dfa import  DFA



def testDfa():
    # test the dfa
    # test the constructor
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
        ('q0','b') : 'q0'
        }      
# 该DFA接受的正则语言L：所有包含偶数个（包括0）a以及偶数个（包括0）个b的字符串，

    dfa = DFA(set(alpahbet), Q, q0, F, delta)

    print("dfa is valid: %s" % dfa.is_valid())
    # 测试 is_accept 函数
    print("dfa is accept 'abab': %s" % dfa.is_accept('abab'))
    print("dfa is accept 'ababab': %s" % dfa.is_accept('ababab'))
    print("dfa is accept 'aaabbb': %s" % dfa.is_accept('aaabbb'))    

    # 测试 run 函数
    print("dfa run 'abab':  " ,  dfa.run('abab'))

testDfa()