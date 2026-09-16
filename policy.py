from dataclasses import dataclass, fields
from enum import Enum

@dataclass
class Policy:
    id: str
    customer: str
    type: str
    premium: float
    status: str

class Type(Enum):
    AUTO = "auto"
    HOME = "home"
    LIFE = "life"


def check_keys(data: list[dict], keys:set[str]) -> list[dict]:
    cleaned_out = []
    for data_el in data:
        data_keys = set(data.keys())
        if data_keys == keys:
            valid= True
            for key in data_keys:
                cleaned = normalize_key(data_el,key)
                if cleaned == None:
                    valid = False
                    continue
                data_el[key] = cleaned
            if not valid:
                continue
            cleaned_out.append(data_el)
    return cleaned_out


def normalize_key(data_el: dict, key:str) -> any:
    value = data_el[key]
    match key:
        case "id":
            if isinstance(value, str):
                return value.upper()
                
        case "customer":
            if isinstance(value,str):
                return value
                
        case "type":
            if isinstance(value,str) and value.lower in [item.value for item in Type]:
                return value.lower
                
        case "premium":
            if isinstance(value,float) or isinstance(value,int):
                return float(value)
                  
        case "status":
            if isinstance(value,str):
                return value

    return None
