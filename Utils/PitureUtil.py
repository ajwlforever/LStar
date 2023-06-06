from graphviz import Digraph
from graphviz import Graph
import torch
import numpy as np



def render_to_pdf(dfa, path):
    # dfa = (alpahbet, Q, q0, F, delta)
    dot = Digraph(comment='Definetion Automata')
    dot.node('S', shape='point')

    # 初始化状态
    for q in dfa.Q:
        dot.node(q, shape='circle') 

    # initial state
    dot.edge('S', dfa.q0)
    # fianl state
    for q in dfa.F:
        dot.node(q, shape='doublecircle')
    
    # transition
    for key in dfa.delta.keys():
        q = key[0]
        a = key[1]
        q_next = dfa.delta[key]
        dot.edge(q, q_next, label=a)
    dot.render(path+'.gv', view=True)

    
    return  

def test_1():
    dot = Digraph(comment='Automata for ab|c')

    dot.node('S', shape='point')
    dot.node('A', shape='circle')
    dot.node('B', shape='doublecircle')
    dot.node('C', shape='circle')
    dot.node('B', shape='circle')

    dot.edge('S', 'A')
    dot.edge('A', 'B', label='a')
    dot.edge('A', 'C', label='c')
    dot.edge('C', 'B', label='b')

    dot.render('Img/automata.gv', view=True)

    
    g = Graph(format='png')



