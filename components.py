# coding: jsx
from pyjsx import jsx, JSX


def Items(items: list[str] = [], **rest) -> JSX:
    return (
        <turbo-frame id="item-list">
            <h3>Items</h3>
        </turbo-frame>
    )

def Main(children, style=None, **rest) -> JSX:
    items = ["a", "b"]
    return (
        <>
            <h1>Todo List</h1>
            <form action="/items" method="post" data-turbo-frame="item-list">
                <input type="text" name="item" placeholder="Add new item..." required />
                <button type="submit">Add</button>
            </form>
            <Items items={items} />
        </>
    )


def Layout(children, **rest) ->  JSX:
    return (
        <>
            <head>
                <script type="module" src="https://cdn.jsdelivr.net/npm/@hotwired/turbo@latest/dist/turbo.es2017-esm.min.js"></script>
            </head>
            <body>{children}</body>
        </>
    )


def App() -> JSX:
    return (
        <Layout>
            <Main>
                <p>This was rendered with PyJSX!</p>
            </Main>
        </Layout>
    )
