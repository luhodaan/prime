from typing import Protocol, List
from src.models import Policy,Country
from decimal import Decimal
from dataclasses import dataclass

class PricingRule(Protocol):
    name:str
    def apply(self, premium: float) -> Decimal:
        ...

@dataclass
class YoungDriverSurcharge():
    max_age: int
    rate: Decimal
    name:str = "young folk"

    def apply(self,premium:float) -> Decimal:
        new_premium = Decimal(premium) * self.rate
        return new_premium

PRICING_RULES: dict[Country,List[PricingRule]] = {
    Country.ITALY.value : [YoungDriverSurcharge(18,Decimal("1.4"))],
    Country.SPAIN.value : [YoungDriverSurcharge(21,Decimal("1.1"))]

}

def rules_engine(parsing_rules: dict[Country,List[PricingRule]],policy:Policy) -> Policy:
    country = policy.country
    country_rules = parsing_rules[country]
    new_premium = policy.premium
    for rule in country_rules:
        new_premium = rule.apply(new_premium) 
    policy.premium = new_premium
    return policy
