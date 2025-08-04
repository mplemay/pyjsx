import pytest

from pyjsx.transpiler import ParseError, transpile


def test_self_closing_non_void_element_causes_loop():
    source = """
# coding: jsx
<head>
    <script type="module" src="https://cdn.jsdelivr.net/npm/@hotwired/turbo@latest/dist/turbo.es2017-esm.min.js" />
</head>
"""
    # We expect a ParseError, but if it loops, pytest will eventually time out.
    # The specific error message might vary depending on where the loop is detected.
    with pytest.raises(ParseError, match="Non-void element <head> cannot be self-closing"):
        transpile(source)
