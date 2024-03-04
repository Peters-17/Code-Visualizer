# server/app.py
import sys
import os

# 将项目根目录（即包含analyzer和visualizer目录的那一级）添加到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyzer.code_analyzer import analyze_code
from visualizer.graph_visualizer import create_graph
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.data.decode("utf-8")
    functions, calls = analyze_code(code)
    # 为了Demo，这里我们直接返回分析结果，实际应用中可能需要进一步处理
    return jsonify({"functions": functions, "calls": calls})

if __name__ == '__main__':
    app.run(debug=True)
