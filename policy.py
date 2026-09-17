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

class InvalidPolicyError(Exception):
    pass

def filter_input_by_keys(data: list[dict], keys:set[str]) -> list[dict]:
    cleaned_out = []
    for i,data_el in enumerate(data):
        data_keys = set(data_el.keys())
        print(f"element{i} has keys {data_keys} vs official {keys}")
        if data_keys == keys:
            valid = True
            print(f"element {i} has valid keys")
            for key in data_keys:
                try:
                    cleaned = normalize_key(data_el,key)
                    if cleaned is None:
                        valid = False
                        break
                except InvalidPolicyError:
                    valid = False
                    break
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
            else:
                print(f"id of type {type(value)}")
                
        case "customer":
            if isinstance(value,str):
                return value
            else:
                print(f"customer type {type(value)}")
                
        case "type":
            if isinstance(value,str) and value.lower() in [item.value for item in Type]:
                return value.lower()
            else:
                print(f"type error for {value}")
                
        case "premium":
            try:
                float(value)
                return float(value)
            except ValueError:
                raise InvalidPolicyError(f"Tried to parse {value} into float without success")
                return None
                  
        case "status":
            if isinstance(value,str):
                return value

    return None

def parse_data(data: list[dict],keys:list[str]) -> list[Policy]:
    cleaned_data = filter_input_by_keys(data, set(keys))
    print(f"cleaned data we have back is {cleaned_data}")
    parsed_data = [Policy(**item) for item in cleaned_data] 
    return parsed_data

def main() -> list[Policy]:
    keys = {field.name for field in fields(Policy)}
    print(f"correct data keys are {keys}")
    raw_data = RAW_POLICIES
    print(f"data import for {raw_data}")
    policies = parse_data(raw_data,keys)
    return policies

if __name__ == "__main__":
    parsed_data = main()
    print(f"final result {parsed_data}")
    print(f"len of final result is {len(parsed_data)}")