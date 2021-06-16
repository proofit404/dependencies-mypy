from typing import Any

class Injector:
    def __init__(self, **kwargs: Any) -> None:
        ...

class Package:
    def __init__(self, name: str) -> None:
        ...

    def __getattr__(self, name: str) -> Any:
        ...
