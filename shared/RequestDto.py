from dataclasses import dataclass

@dataclass
class RequestDto:
    url: str
    type: str
    title: str