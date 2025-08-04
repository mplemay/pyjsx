# PyJSX Project Overview for LLM Agents

This document provides a detailed overview of the PyJSX project, its architecture, core functionalities, and operational guidelines for an LLM agent to effectively understand and interact with the codebase.

## 1. Project Name and Purpose

**Project Name:** PyJSX (python-jsx)

**Purpose:** PyJSX is a Python library designed to enable the use of JSX (JavaScript XML) syntax directly within Python code. It acts as a transpiler, converting JSX into standard Python function calls that generate HTML or other structured output. This allows for a declarative, component-based approach to generating UI elements or structured data within a Python environment, similar to how JSX is used with React in JavaScript.

## 2. Core Functionality

PyJSX's core functionality revolves around the transpilation of JSX syntax embedded in Python files into executable Python code. This is achieved through two primary integration methods:

*   **`# coding: jsx` directive**: Python files (`.py`) can include JSX by adding `# coding: jsx` at the top. A custom codec intercepts these files during import, transpiling the JSX before execution.
*   **`.px` file extension**: Files with a `.px` extension are automatically recognized by a custom import hook. When imported, their JSX content is transpiled into Python.

The transpiled JSX is converted into calls to the `pyjsx.jsx()` function, which then handles the rendering of elements, components, and fragments into their final string representation (e.g., HTML).

## 3. Architecture and Key Components

The PyJSX codebase is structured into several modules, each responsible for a specific part of the transpilation and rendering pipeline:

*   **`pyjsx/__init__.py`**:
    *   Initializes the `pyjsx` package.
    *   Defines the package version (`__version__`).
    *   Exposes key public APIs: `JSX`, `JSXComponent`, `jsx`, `register_jsx`, `transpile`.

*   **`pyjsx/__main__.py`**:
    *   Provides a command-line interface for transpiling Python files or directories containing JSX.
    *   Useful for debugging or pre-processing JSX files outside of the import system.

*   **`pyjsx/auto_setup.py`**:
    *   Simplifies the setup process by automatically registering both the `jsx` codec and the `.px` import hook.
    *   Importing this module (`import pyjsx.auto_setup`) is typically the first step in any application using PyJSX.

*   **`pyjsx/codec_hook.py`**:
    *   Implements the custom Python codec named `jsx`.
    *   Intercepts files marked with `# coding: jsx` and uses the `transpiler.py` to convert their content before Python's standard execution.

*   **`pyjsx/elements.py`**:
    *   Defines sets of known HTML `void_elements` (self-closing tags like `<img />`) and `builtin_elements` (standard HTML tags).
    *   Provides utility functions (`is_void_element`, `is_builtin_element`) used by the `jsx.py` module for correct HTML rendering.

*   **`pyjsx/import_hook.py`**:
    *   Implements a `MetaPathFinder` and `FileLoader` to handle `.px` files.
    *   When a `.px` file is imported, it uses the `transpiler.py` to convert the JSX content into Python code, which is then executed as a module.

*   **`pyjsx/jsx.py`**:
    *   Contains the core runtime logic for rendering JSX.
    *   Defines the `jsx()` function, which is the target of the transpilation. This function takes a tag (string for native elements, callable for custom components), a dictionary of props, and a list of children.
    *   Manages `JSXElement`, `JSXComponent`, and `JSXFragment` classes, responsible for converting the parsed JSX structure into a string (e.g., HTML).
    *   Handles prop processing (e.g., `style` dictionaries to CSS strings, boolean props).

*   **`pyjsx/mypy.py`**:
    *   Provides a MyPy plugin that enables MyPy to correctly parse and type-check Python files containing JSX syntax.
    *   This ensures static analysis and type safety even with embedded JSX.

*   **`pyjsx/tokenizer.py`**:
    *   The lexical analyzer (tokenizer) for PyJSX.
    *   Takes raw source code as input and breaks it down into a stream of `Token` objects (e.g., `ELEMENT_NAME`, `JSX_OPEN`, `ATTRIBUTE`).
    *   Manages different parsing modes (Python, JSX, F-string) to correctly identify and categorize tokens.
    *   Includes error handling for syntax errors during tokenization.

*   **`pyjsx/transpiler.py`**:
    *   The main transpilation engine.
    *   Uses the `Tokenizer` to get tokens.
    *   Parses the token stream into an Abstract Syntax Tree (AST) representation of JSX elements (`JSXElement`, `JSXFragment`, `JSXNamedAttribute`, `JSXSpreadAttribute`, `JSXText`, `JSXExpression`).
    *   Converts this AST into Python code that calls the `jsx()` function from `pyjsx/jsx.py`.

*   **`pyjsx/util.py`**:
    *   Contains various utility functions used across the project.
    *   Examples include `indent` for formatting, `flatten` for processing nested lists of children, and `get_line_number_offset`/`highlight_line` for error reporting.

## 4. Integration Methods (Examples)

The `examples/` directory showcases how to use PyJSX with both the `codec` and `import_hook` mechanisms. Each example demonstrates a specific feature:

*   **`custom_components_codec/` & `custom_components_import_hook/`**:
    *   Demonstrate defining and using custom Python functions as JSX components.
    *   `custom.py` (codec) uses `# coding: jsx`.
    *   `custom.px` (import hook) uses the `.px` extension.
    *   `main.py` in both cases imports `pyjsx.auto_setup` and then the component file.

*   **`props_codec/` & `props_import_hook/`**:
    *   Illustrate various ways to pass and handle props, including boolean props, dictionary-based `style` props, and passing JSX elements as props.
    *   `props.py` (codec) and `props.px` (import hook) contain the component definitions.

*   **`table_codec/` & `table_import_hook/`**:
    *   Show how to dynamically generate complex HTML structures (like tables) using Python logic (e.g., list comprehensions) embedded within JSX.
    *   `table.py` (codec) and `table.px` (import hook) contain the table generation logic.

## 5. Development Environment and Operations

### Setting up the Environment:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/tomasr8/pyjsx.git
    cd pyjsx
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
3.  **Install dependencies (including development tools):**
    ```bash
    pip install -e ".[dev]"
    ```

### Running Tests:

The project uses `pytest` for testing, with `pytest-snapshot` for snapshot testing.

*   **Run all tests:**
    ```bash
    pytest
    ```
*   **Run tests without coverage (faster):**
    ```bash
    pytest --no-cov
    ```
*   **Updating snapshots:** If tests fail due to intentional changes in output, you might need to update snapshots:
    ```bash
    pytest --snapshot-update
    ```
    **Caution:** Always review `git diff` after updating snapshots to ensure only expected changes are committed.

### Linting and Formatting:

The project uses `ruff` for linting and formatting.

*   **Run lint checks:**
    ```bash
    ruff check pyjsx/ tests/
    ```
*   **Automatically fix linting issues:**
    ```bash
    ruff check pyjsx/ tests/ --fix
    ```
*   **Format code:**
    ```bash
    ruff format pyjsx/ tests/
    ```

### Type Checking:

The project uses `pyright` for static type checking.

*   **Run type checks:**
    ```bash
    pyright
    ```

### Running Examples:

Each example can be run by navigating to its directory and executing its `main.py` file:

```bash
cd examples/custom_components_codec/
python main.py
```

### Manual Transpilation:

You can manually transpile a file or directory using the `pyjsx/__main__.py` script:

```bash
python -m pyjsx path/to/your_file.py
python -m pyjsx path/to/your_directory/
```
This will create new files with `_transpiled` in their name (e.g., `your_file_transpiled.py`).

## 6. Important Considerations for LLM Agents

When operating within the PyJSX codebase, adhere to the following guidelines:

*   **Absolute Paths**: Always use absolute paths when interacting with the file system (e.g., `read_file`, `write_file`). The project root is `/Users/mattlemay/Github/pyjsx`.
*   **Code Style and Standards**:
    *   Strictly adhere to the code style enforced by `ruff` and `pyright`.
    *   Run `ruff check --fix` and `pyright` after making changes to ensure compliance.
    *   Mimic existing code patterns, naming conventions, and architectural choices.
*   **Testing is Paramount**:
    *   **Always run relevant tests** after making any code changes.
    *   If adding new features, consider adding new test cases.
    *   Understand the purpose of snapshot tests and how to update them responsibly.
*   **No Assumptions**: Never assume the content of a file. Always use `read_file` or `read_many_files` to inspect file contents before making modifications or drawing conclusions.
*   **JSX Syntax**: Refer to the `README.md` and `pyjsx/tokenizer.py` for the supported JSX grammar. Be mindful of how JSX elements, attributes, and embedded Python expressions are structured.
*   **Transpilation Logic**: When modifying the transpilation process (`tokenizer.py`, `transpiler.py`), understand the impact on both the `codec_hook` and `import_hook` mechanisms.
*   **Runtime Behavior**: Changes to `pyjsx/jsx.py` directly affect how JSX is rendered at runtime. Ensure that any modifications maintain compatibility and correct output.
*   **Error Handling**: Pay attention to error messages from the tokenizer and transpiler. They often provide precise locations and reasons for parsing failures.
*   **Virtual Environment**: All Python operations should ideally be performed within the activated virtual environment (`.venv`).
*   **Git Operations**: When asked to commit changes, always inspect `git status` and `git diff` first. Propose clear and concise commit messages.
*   **User Confirmation**: For any significant changes or actions that modify the codebase or system state, explain the action and seek user confirmation.
