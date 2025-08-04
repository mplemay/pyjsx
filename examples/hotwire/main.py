from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from pyjsx.jsx import JSX
import pyjsx.auto_setup
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.mount("/javascript", StaticFiles(directory="javascript"), name="javascript")
app.mount("/static", StaticFiles(directory="static"), name="static")

class JSXResponse(HTMLResponse):
    def render(self, content: JSX) -> bytes:
        return super().render(str(content))

class TurboStreamResponse(HTMLResponse):
    media_type = "text/vnd.turbo-stream.html"

    def render(self, content: JSX) -> bytes:
        return super().render(str(content))

from pyjsx_components.pages import HomePage
from pyjsx_components.layout import Layout
from pyjsx_components.turbo_streams import TurboStreamRemove
from pyjsx.jsx import jsx

@app.get("/", response_class=JSXResponse)
async def read_root(request: Request):
    user_data = {"name": "World"}
    page_content = HomePage(user=user_data)
    full_html = Layout(children=page_content, title="Welcome to PyJSX App")
    return full_html

@app.post("/items/{item_id}/delete", response_class=TurboStreamResponse)
async def delete_item(item_id: str):
    print(f"Deleting item: {item_id}")
    return TurboStreamRemove(target=jsx.dom_id({"id": item_id, "type": "item"}))

@app.websocket("/cable")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received from client: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"WebSocket error: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
