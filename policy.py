from dataclasses import dataclass, fields
from enum import Enum
from data import RAW_POLICIES

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
        data_keys = set(data_el.keys())
        if data_keys == keys:
            valid= True
            for key in data_keys:
                cleaned = normalize_key(data_el,key)
                if cleaned is None:
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
                return value
                
        case "customer":
            if isinstance(value,str):
                return value
                
        case "type":
            if isinstance(value,str) and value.lower in [item.value for item in Type]:
                return value.lower()
                
        case "premium":
            try:
                float(value)
                return float(value)
            except ValueError:
                return None
                  
        case "status":
            if isinstance(value,str):
                return value

    return None

def parse_data(data: list[str],keys:list[str]) -> list[Policy]:
    cleaned_data = check_keys(data, keys)
    parsed_data = [Policy(**item) for item in cleaned_data] 
    return parsed_data

def main() -> list[Policy]:
    keys = [field.name for field in fields(Policy)]
    raw_data = RAW_POLICIES
    policies = parse_data(raw_data,keys)
    return policies
