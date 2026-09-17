from policy import (
    Policy,
    Type,
    filter_input_by_keys,
    normalize_key,
    parse_data,
    main,
    InvalidPolicyError
)
from dataclasses import dataclass,fields

from data import RAW_POLICIES
import pytest

def test_invalid_premium():
    raw_data_el = RAW_POLICIES[3]
    keys = {field.name for field in fields(Policy)}
    result = filter_input_by_keys([raw_data_el],keys)
    assert [] == result

def test_invalid_premium_exception():
    raw_data_el = RAW_POLICIES[3]
    keys = {field.name for field in fields(Policy)}
    with pytest.raises(InvalidPolicyError):
        normalize_key(raw_data_el,"premium")