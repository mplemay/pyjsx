# coding: jsx
from pyjsx import jsx, JSX


def Items(items: list[str] = [], **rest) -> JSX:
    return (
        jsx("turbo-frame", {'id': "item-list"}, [jsx("h3", {}, ["Items"])])
    )

def Main(children, style=None, **rest) -> JSX:
    items = ["a", "b"]
    return (
        jsx(jsx.Fragment, {}, [jsx("h1", {}, ["Todo List"]), jsx("form", {'action': "/items", 'method': "post", 'data-turbo-frame': "item-list"}, [jsx("input", {'type': "text", 'name': "item", 'placeholder': "Add new item...", 'required': True}, []), jsx("button", {'type': "submit"}, ["Add"])]), jsx(Items, {'items': items}, [])])
    )


def Layout(children, **rest) ->  JSX:
    return (
        jsx(jsx.Fragment, {}, [jsx("head", {}, [jsx("script", {'type': "module", 'src': "https://cdn.jsdelivr.net/npm/@hotwired/turbo@latest/dist/turbo.es2017-esm.min.js"}, [])]), jsx("body", {}, [children])])
    )


def App() -> JSX:
    return (
        jsx(Layout, {}, [jsx(Main, {}, [jsx("p", {}, ["This was rendered with PyJSX!"])])])
    )
