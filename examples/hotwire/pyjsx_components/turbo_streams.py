# coding: jsx
from pyjsx import jsx, JSX

def TurboStream(action: str, target: str | None = None, content: JSX | None = None, **rest) -> JSX:
    """
    Base Turbo Stream component.
    """
    attrs = {"action": action}
    if target:
        attrs["target"] = target
    return (
        <turbo-stream {...attrs}>
            {content}
        </turbo-stream>
    )

def TurboStreamAppend(target: str, content: JSX, **rest) -> JSX:
    return TurboStream(action="append", target=target, content=content)

def TurboStreamPrepend(target: str, content: JSX, **rest) -> JSX:
    return TurboStream(action="prepend", target=target, content=content)

def TurboStreamReplace(target: str, content: JSX, **rest) -> JSX:
    return TurboStream(action="replace", target=target, content=content)

def TurboStreamUpdate(target: str, content: JSX, **rest) -> JSX:
    return TurboStream(action="update", target=target, content=content)

def TurboStreamRemove(target: str, **rest) -> JSX:
    return TurboStream(action="remove", target=target)

def TurboStreamBefore(target: str, content: JSX, **rest) -> JSX:
    return TurboStream(action="before", target=target, content=content)

def TurboStreamAfter(target: str, content: JSX, **rest) -> JSX:
    return TurboStream(action="after", target=target, content=content)