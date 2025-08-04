# coding: jsx
from pyjsx import jsx, JSX # Import jsx to access its helpers

def ItemListFrame(items: list[str], **rest) -> JSX:
    return (
        <turbo-frame id={jsx.dom_id({"type": "item-list"})}>
            <h3>Items</h3>
            <ul>
                {[<li key={item} id={jsx.dom_id({"id": item, "type": "item"})}>{item}</li> for item in items]}
            </ul>
        </turbo-frame>
    )

def GreetableDiv(name: str, **rest) -> JSX:
    return (
        <div data-controller="hello" data-hello-name-value={name}>
            <span data-hello-target="output"></span>
            <button data-action="click->hello#greet">Say Hello</button>
        </div>
    )

def DeleteButton(item_id: str, **rest) -> JSX:
    return (
        <button
            data-turbo-method="post"
            data-turbo-confirm="Are you sure?"
            data-turbo-frame="_top" # Target the top frame for full page refresh or specific frame
            data-action="click->item#delete" # Example Stimulus action
            hx-post={f"/items/{item_id}/delete"}
        >
            Delete Item
        </button>
    )