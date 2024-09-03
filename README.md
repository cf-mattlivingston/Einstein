# Einstein
Static Code Analyzer

Einstein is a Python-based static code analyzer designed to identify common issues in your Python code. It scans your code for unused imports, long lines, missing docstrings, unused variables, and more. Use Einstein to ensure your codebase follows best practices and maintains high quality.

Features

	•	Unused Imports: Detects and reports imports that are not used in the code.
	•	Long Lines: Flags lines that exceed a specified length (default is 79 characters).
	•	Missing Docstrings: Identifies functions and classes that lack docstrings.
	•	Unused Variables: Checks for variables that are defined but never used.
	•	Wildcard Imports: Warns against the use of wildcard imports (e.g., from module import *).

Installation

To use Einstein, simply clone the repository and run the script. There are no external dependencies required beyond Python itself.

```bash
git clone https://github.com/cf-mattlivingston/einstein.git
cd einstein

```

# Usage

You can use Einstein to analyze individual Python files or entire directories.

Analyze a Single File

To analyze a specific file, run:

```bash
python einstein.py example.py
```

Replace example.py with the path to the file you want to analyze.

Analyze a Directory

To analyze all Python files within a directory and its subdirectories, run:

```bash
python einstein.py --dir /path/to/your/directory
```

# Configuration

Line Length

By default, Einstein flags lines that exceed 79 characters. You can adjust this by modifying the max_length parameter in the check_line_length method.

Custom Checks

Einstein is designed to be easily extensible. You can add your own custom checks by extending the CodeAnalyzer class with additional methods.

Example Output

Running Einstein on a sample file might yield the following output:

```bash
Issues found in example.py:
Missing docstring in function 'foo' at line 10
Unused import 'os' at line 2
Line 15 exceeds 79 characters
Unused variable 'unused_var' at line 20
```

# Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Contact

For questions or support, please reach out to your.email@example.com.

This README provides a comprehensive overview of Einstein, including installation, usage, and customization instructions. You can tailor the details (like the repository URL or contact email) to match your project specifics.
