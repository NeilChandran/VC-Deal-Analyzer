import pandas as pd

class FinancialStatement:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)
        self.balance_sheet = self.data[self.data['Type'] == 'BalanceSheet']
        self.income_statement = self.data[self.data['Type'] == 'IncomeStatement']
        self.cash_flow = self.data[self.data['Type'] == 'CashFlow']

    def calc_profit_margin(self):
        net_income = float(self.income_statement[self.income_statement['LineItem']=='NetIncome']['Value'])
        revenue = float(self.income_statement[self.income_statement['LineItem']=='Revenue']['Value'])
        if revenue == 0:
            return 0
        return net_income / revenue

    def debt_to_equity(self):
        debt = float(self.balance_sheet[self.balance_sheet['LineItem']=='TotalDebt']['Value'])
        equity = float(self.balance_sheet[self.balance_sheet['LineItem']=='ShareholdersEquity']['Value'])
        if equity == 0:
            return float('inf')
        return debt / equity

    # (Add: liquidity ratios, growth rates, custom scoring, etc.)

if __name__ == "__main__":
    fs = FinancialStatement("../data/sample_startup_data.csv")
    print("Profit Margin:", fs.calc_profit_margin())
    print("Debt/Equity:", fs.debt_to_equity())

