import ast
import networkx as nx
import matplotlib.pyplot as plt

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.G = nx.DiGraph()
        self.current_class = None
        self.current_function = None  # Add this attribute to keep track of the current function

    def visit_ClassDef(self, node):
        # Add the class as a node and make it the current context
        self.G.add_node(node.name, type='class', color='lightblue', shape='box')
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = None
    
    def visit_FunctionDef(self, node):
        function_name = f"{self.current_class}.{node.name}" if self.current_class else node.name
        self.G.add_node(function_name, type='function', color='lightgreen')
        self.current_function = function_name  # Set the current function
        if self.current_class:
            # If we're in a class context, add an edge from the class to the method
            self.G.add_edge(self.current_class, function_name, type='contains')
        self.generic_visit(node)
        self.current_function = None  # Reset the current function
    
    def visit_Call(self, node):
        caller_name = self.current_function if self.current_function else self.current_class
        callee = None
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
            callee = f"{node.func.value.id}.{node.func.attr}"
        elif isinstance(node.func, ast.Name):
            callee = node.func.id
        if caller_name and callee:
            self.G.add_edge(caller_name, callee, type='calls')
        self.generic_visit(node)
    
    def visit_Assign(self, node):
        if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
            instance_name = ''.join([target.id for target in node.targets if isinstance(target, ast.Name)])
            class_name = node.value.func.id
            self.G.add_node(instance_name, type='instance', color='orange')
            self.G.add_edge(instance_name, class_name, type='instance_of')
        self.generic_visit(node)

def analyze_code(file_path):
    with open(file_path, "r") as source:
        node = ast.parse(source.read(), filename=file_path)
        analyzer = CodeAnalyzer()
        analyzer.visit(node)

        # Set node color based on type, use a default color if 'color' is not present
        default_color = 'grey'
        node_colors = [data.get('color', default_color) for _, data in analyzer.G.nodes(data=True)]

        # Draw the graph
        pos = nx.spring_layout(analyzer.G)
        nx.draw(analyzer.G, pos, with_labels=True, node_color=node_colors, arrows=True)
        
        # Draw edge labels
        edge_labels = {(u, v): data['type'] for u, v, data in analyzer.G.edges(data=True) if 'type' in data}
        nx.draw_networkx_edge_labels(analyzer.G, pos, edge_labels=edge_labels)
        
        plt.show()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python code_analyzer.py <path_to_python_file>")
    else:
        analyze_code(sys.argv[1])
