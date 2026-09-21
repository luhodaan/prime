from src.main import (
    Policy,
    Type,
    filter_input_by_keys,
    normalize_key,
    parse_data,
    main,
    InvalidPolicyError,
    parse_policy
)
from dataclasses import dataclass,fields

from src.data import RAW_POLICIES
import pytest

from src.aggregators import total_premium_by_type

@pytest.fixture
def raw_data_no_premium():
    return RAW_POLICIES[3]

@pytest.fixture
def raw_data_el_complete():
    return RAW_POLICIES[1]

@pytest.fixture
def keys():
    return {field.name for field in fields(Policy)} 

def test_invalid_premium(raw_data_no_premium,keys):
    result = filter_input_by_keys([raw_data_no_premium],keys)
    assert [] == result

def test_invalid_premium_exception(raw_data_no_premium):
    with pytest.raises(InvalidPolicyError):
        normalize_key(raw_data_no_premium,"premium")

def test_total_premium(keys):
    raw_data = RAW_POLICIES[:3]
    policies = parse_data(raw_data,keys)
    total = total_premium_by_type(policies)
    assert 910.50 == total

def test_country_not_null(raw_data_el_complete):
    policy = parse_policy(raw_data_el_complete)
    assert policy.country is not None


