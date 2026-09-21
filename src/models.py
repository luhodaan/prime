from dataclasses import dataclass
from enum import Enum

@dataclass
class Policy:
    id: str
    customer: str
    type: str
    premium: float
    status: str
    country: str

class Type(Enum):
    AUTO = "auto"
    HOME = "home"
    LIFE = "life"

class Country(Enum):
    ITALY = "italy"
    SPAIN = "spain"
    UK = "uk"    