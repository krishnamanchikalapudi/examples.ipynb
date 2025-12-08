"""Utility helpers for MCP/agent notebooks

Provides a minimal format_messages function used by example notebooks.
"""
from typing import Any, Dict, List, Union

MessageLike = Union[str, Dict[str, Any], List[Any], tuple]


def format_messages(messages: Union[MessageLike, List[MessageLike]]) -> List[Dict[str, str]]:
    """Normalize messages into a list of dicts with 'role' and 'content'.

    Accepts:
      - a single string (treated as user content)
      - a single dict {'role':..., 'content':...}
      - a list of such items
      - tuples or lists like (role, content)

    Returns:
      - list of {'role': str, 'content': str}
    """
    if messages is None:
        return []

    # If single string -> wrap
    if isinstance(messages, str):
        return [{"role": "user", "content": messages}]

    # If a single dict-like message
    if isinstance(messages, dict) and ("role" in messages or "content" in messages):
        role = str(messages.get("role", "user"))
        content = str(messages.get("content", ""))
        return [{"role": role, "content": content}]

    # If it's a tuple/list representing a single message
    if isinstance(messages, (list, tuple)) and messages and not any(isinstance(x, (list, tuple, dict)) for x in messages):
        # treat as (role, content)
        try:
            role = str(messages[0])
            content = str(messages[1])
            return [{"role": role, "content": content}]
        except Exception:
            return [{"role": "user", "content": str(messages)}]

    # Otherwise assume iterable/list of messages
    out: List[Dict[str, str]] = []
    try:
        for m in messages:  # type: ignore
            if isinstance(m, str):
                out.append({"role": "user", "content": m})
            elif isinstance(m, dict):
                role = str(m.get("role", "user"))
                content = str(m.get("content", ""))
                out.append({"role": role, "content": content})
            elif isinstance(m, (list, tuple)) and len(m) >= 2:
                out.append({"role": str(m[0]), "content": str(m[1])})
            else:
                out.append({"role": "user", "content": str(m)})
    except TypeError:
        # Fallback: convert entire object to a single message
        out = [{"role": "user", "content": str(messages)}]

    return out
