
from jinja2 import Template

class DealMemo:
    def __init__(self, company, financials, cap_table, pros, risks):
        self.company = company
        self.financials = financials
        self.cap_table = cap_table
        self.pros = pros
        self.risks = risks

    def generate(self):
        template = Template("""
        # Deal Memo: {{ company }}
        ## Financial Overview
        - Revenue: {{ financials['revenue'] }}
        - Profit Margin: {{ financials['profit_margin'] }}
        ## Cap Table Post-Round
        {% for shareholder, shares in cap_table.items() %}
        - {{ shareholder }}: {{ shares }} shares
        {% endfor %}
        ## Investment Pros
        {{ pros }}
        ## Investment Risks
        {{ risks }}
        """)
        return template.render(**self.__dict__)

# (Extend: auto-populate from analytics, output files, 100+ LOC)
