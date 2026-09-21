from dataclasses import dataclass,fields

from src.data import RAW_POLICIES
import pytest

from src.aggregators import total_premium_by_type
from src.models import Policy

from src.rules import rules_engine, PRICING_RULES

@pytest.fixture
def raw_data_no_premium():
    return RAW_POLICIES[3]

@pytest.fixture
def raw_data_el_complete():
    return RAW_POLICIES[1]

@pytest.fixture
def keys():
    return {field.name for field in fields(Policy)}

@pytest.fixture
def policy_object():
    policy = Policy(id="P002", customer="giulia", type= "home", premium=180.00, status= "active",country="spain")
    return policy 

def test_rule_engine(policy_object):
    policy = rules_engine(PRICING_RULES,policy_object)
    assert 198 == policy.premium