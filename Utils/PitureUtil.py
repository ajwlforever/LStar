from graphviz import Digraph
from graphviz import Graph
import torch
import numpy as np

dot = Digraph(comment='Automata for ab|c')

dot.node('S', shape='point')
dot.node('A', shape='circle')
dot.node('B', shape='doublecircle')
dot.node('C', shape='circle')

dot.edge('S', 'A')
dot.edge('A', 'B', label='a')
dot.edge('A', 'C', label='c')
dot.edge('C', 'B', label='b')

dot.render('automata.gv', view=True)

 


g = Graph(format='png')


