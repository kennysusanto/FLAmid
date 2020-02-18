from graphviz import Digraph

g = Digraph('G', filename='hello.gv', directory='graphs')
g.attr(rankdir='LR')

g.attr('node', shape='doublecircle')
g.node('s8')

g.attr('node', shape='circle')
g.edge('s1', 's2', label='e')
g.edge('s2', 's3', label='e')
g.edge('s2', 's4', label='e')
g.edge('s3', 's5', label='a')
g.edge('s4', 's6', label='b')
g.edge('s5', 's7', label='e')
g.edge('s6', 's7', label='e')
g.edge('s7', 's8', label='e')
g.edge('s7', 's2', label='e')
g.edge('s1', 's8', label='e')


g.view()