from policy import Policy

def total_premium_by_type(data: list[Policy]) -> float:
        total_premium = 0
        for policy in data:
                if policy.status == "active":
                        total_premium += policy.premium
        return total_premium
