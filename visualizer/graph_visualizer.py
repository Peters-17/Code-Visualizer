# visualizer/graph_visualizer.py
from graphviz import Digraph

def create_graph(functions, calls):
    dot = Digraph(comment='The System Structure')
    
    for func in functions:
        dot.node(func, func)

    for call in set(calls):
        if call in functions:
            dot.edge(func, call)
    
    print(dot.source)
    dot.render('output/system_structure.gv', view=True)
