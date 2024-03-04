# Code Visualizer

## Project Overview

Code Visualizer is a tool designed to help developers understand the structure and relationships within their codebase. By generating interactive graphical representations of classes, functions, and method calls, Code Visualizer aims to provide clear insights into code organization and dependencies.

### Current Features

- **Code Structure Analysis**: Parses Python code to extract classes, functions, and their relationships.
- **Interactive Graphs**: Generates an interactive graph that visualizes the relationships between different parts of the code.
- **Class and Method Grouping**: Classes and their methods are grouped together in the visualization for better clarity.
- **Instance Visualization**: Class instances and their connections to their respective classes are displayed.
- **Function Call Representation**: Function and method calls are clearly represented, showing the flow of the code.

### Usage

To use the Code Visualizer, run the `code_analyzer.py` script with a Python file as an argument:

```bash
python .\analyzer\code_analyzer.py .\test\example.py
```

This will parse the example.py file and open an interactive window displaying the code structure as a graph.

### Future Development Goals

- **Language Support**: Extend support to additional programming languages beyond Python.
- **Code Metric**s: Integrate code complexity and quality metrics into the visualization.
- **Version Control Integration**: Offer insights into code changes over time by integrating with version control systems like Git.
- **Customization Options**: Enable users to customize the visualization, such as altering colors, shapes, and layout algorithms.
- **Enhanced Interaction**: Improve the graph's interactive features, such as search functionality and detailed information on hover or click.

Performance Optimization: Enhance performance for analyzing large codebases with minimal latency.
### Contributing

Contributions to Code Visualizer are welcome! If you have suggestions or want to contribute to the development of the project, please create an issue or pull request in the repository.
