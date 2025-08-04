from fastapi.responses import HTMLResponse

from pyjsx.jsx import JSX


class JSXResponse(HTMLResponse):
    """
    A custom FastAPI response class that renders PyJSX JSX objects to HTML.
    Allows returning JSX objects directly from route functions.
    """

    def render(self, content: JSX) -> bytes:
        # PyJSX's JSX objects have a __str__ method that renders them to HTML.
        # We call str() on the content before passing it to the superclass's render method.
        return super().render(str(content))


class TurboStreamResponse(HTMLResponse):
    """
    A custom FastAPI response class for Turbo Stream responses.
    Sets the Content-Type header to 'text/vnd.turbo-stream.html'.
    """

    media_type = "text/vnd.turbo-stream.html"

    def render(self, content: JSX) -> bytes:
        # Ensure the content is a Turbo Stream JSX object
        # PyJSX's JSX objects have a __str__ method that renders them to HTML.
        return super().render(str(content))
