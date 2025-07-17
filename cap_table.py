import pandas as pd

class CapTable:
    def __init__(self, founders=3, shares=1000000):
        self.shareholders = {"Founder" + str(i+1): shares//founders for i in range(founders)}
        self.total_shares = shares

    def add_investor(self, name, investment, price_per_share):
        shares = int(investment / price_per_share)
        self.shareholders[name] = self.shareholders.get(name, 0) + shares
        self.total_shares += shares

    def simulate_round(self, new_investor, investment, pre_money_valuation):
        price_per_share = pre_money_valuation / self.total_shares
        self.add_investor(new_investor, investment, price_per_share)
        return self.shareholders

    def compute_dilution(self, original_owner):
        return self.shareholders[original_owner] / self.total_shares
