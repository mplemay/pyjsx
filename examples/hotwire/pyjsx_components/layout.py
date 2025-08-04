# coding: jsx
from pyjsx import jsx, JSX

def Layout(children, title="My App", **rest) -> JSX:
    return (
        <html>
            <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <title>{title}</title>
                <link rel="stylesheet" href="/static/app.css" />
                {/* Load the main JavaScript entry point, which includes Hotwire */}
                <script type="module" src="/javascript/application.js"></script>
            </head>
            <body>
                {children}
            </body>
        </html>
    )