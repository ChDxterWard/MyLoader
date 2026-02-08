from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass

@dataclass
class RequestDto:
    url: str
    type: str