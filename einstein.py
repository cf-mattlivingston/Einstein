import ast
import os

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self, filename):
        self.filename = filename
        self.issues = []

    def visit_FunctionDef(self, node):
        # Check for missing docstrings in functions
        if not ast.get_docstring(node):
            self.issues.append(f"Missing docstring in function '{node.name}' at line {node.lineno}")
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        # Check for missing docstrings in classes
        if not ast.get_docstring(node):
            self.issues.append(f"Missing docstring in class '{node.name}' at line {node.lineno}")
        self.generic_visit(node)

    def visit_Import(self, node):
        # Check for unused imports
        for alias in node.names:
            if alias.asname:
                name = alias.asname
            else:
                name = alias.name
            if not self._is_name_used(node, name):
                self.issues.append(f"Unused import '{name}' at line {node.lineno}")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        # Check for wildcard imports
        if node.names[0].name == "*":
            self.issues.append(f"Wildcard import in '{node.module}' at line {node.lineno}")
        else:
            self.visit_Import(node)

    def visit_Assign(self, node):
        # Check for unused variables
        for target in node.targets:
            if isinstance(target, ast.Name):
                if not self._is_name_used(node, target.id):
                    self.issues.append(f"Unused variable '{target.id}' at line {node.lineno}")
        self.generic_visit(node)

    def _is_name_used(self, node, name):
        """Helper method to check if a name is used after its definition."""
        for sibling in ast.walk(node):
            if isinstance(sibling, ast.Name) and sibling.id == name and isinstance(sibling.ctx, ast.Load):
                return True
        return False

    def check_line_length(self, line, lineno, max_length=79):
        if len(line) > max_length:
            self.issues.append(f"Line {lineno} exceeds {max_length} characters")

    def report(self):
        if not self.issues:
            print(f"No issues found in {self.filename}")
        else:
            print(f"Issues found in {self.filename}:")
            for issue in self.issues:
                print(issue)

def analyze_file(filename):
    with open(filename, "r") as file:
        source = file.read()

    analyzer = CodeAnalyzer(filename)
    tree = ast.parse(source)
    analyzer.visit(tree)

    # Check for long lines
    for lineno, line in enumerate(source.splitlines(), start=1):
        analyzer.check_line_length(line, lineno)

    analyzer.report()

def analyze_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                analyze_file(os.path.join(root, file))

if __name__ == "__main__":
    # Example usage: Analyze a single file or a directory
    analyze_file("example.py")  # Replace with the file you want to analyze
    # analyze_directory("path/to/directory")  # Uncomment to analyze a directory
