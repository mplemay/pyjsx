# coding: jsx
from pyjsx import jsx, JSX

def HomePage(user: dict, **rest) -> JSX:
    return (
        <div>
            <h1>Hello, {user["name"]}!</h1>
            <p>Welcome to your PyJSX-powered FastAPI application with Hotwire.</p>
            <div id={jsx.dom_id({"type": "item-list"})}>
                <h3>Items</h3>
                <ul>
                    <li id={jsx.dom_id({"id": "123", "type": "item"})}>Item 123</li>
                    <li id={jsx.dom_id({"id": "456", "type": "item"})}>Item 456</li>
                </ul>
            </div>
            <button data-turbo-method="post" data-turbo-confirm="Are you sure?" data-turbo-frame="_top" data-action="click->item#delete" hx-post="/items/123/delete">Delete Item 123</button>
        </div>
    )