import numpy_financial as npf


class Evaluator:
    """
    Evaluates the financial viability of a real estate investment.
    """

    def __init__(
        self,
        buy_price,
        monthly_rental_income,
        property_tax,
        annual_coproperty_fees,
        loan_calculator,
        works_price=0,
        management_fees=0,
        holding_years=20,
        resale_value=None,
    ):
        self.buy_price = buy_price  # Prix d'achat sans travaux
        self.works_price = works_price  # Coût des travaux
        self.property_total_value = buy_price + works_price  # Prix total avec travaux
        self.monthly_rental_income = monthly_rental_income
        self.property_tax = property_tax
        self.annual_coproperty_fees = annual_coproperty_fees
        self.management_fees = management_fees
        self.loan_calculator = loan_calculator
        self.holding_years = holding_years
        # Valeur de revente après holding_years, par défaut valorisation à 2% par an
        self.resale_value = resale_value or buy_price * (1.02**holding_years)

    def calculate_monthly_cash_flow(self):
        """
        Calculate the monthly cash flow after all expenses and loan payment.
        """
        monthly_expenses = (
            self.property_tax / 12
            + self.annual_coproperty_fees / 12
            + self.management_fees
            + self.loan_calculator.calculate_monthly_payment(self.property_total_value)
        )
        return self.monthly_rental_income - monthly_expenses

    def calculate_irr(self):
        """
        Calculate the Internal Rate of Return (IRR) over the holding period.
        """
        nb_months = self.holding_years * 12
        monthly_cashflow = self.calculate_monthly_cash_flow()

        cash_flows = [-self.loan_calculator.borrower.apport]  # Apport initial (sortie)
        cash_flows += [monthly_cashflow] * nb_months  # Cashflows mensuels
        cash_flows[-1] += self.resale_value  # Valeur de revente en dernier flux

        irr = npf.irr(cash_flows)
        return irr * 12 * 100  # IRR annualisé en %

    def evaluate_rentability(self):
        """
        Return key financial indicators.
        """
        gross_profitability = (self.monthly_rental_income * 12 / self.buy_price) * 100
        net_profitability = (
            self.calculate_monthly_cash_flow() * 12 / self.property_total_value
        ) * 100
        irr = self.calculate_irr()

        return {
            "gross_profitability": round(gross_profitability, 2),
            "net_profitability": round(net_profitability, 2),
            "monthly_cash_flow": round(self.calculate_monthly_cash_flow(), 2),
            "monthly_rent": self.monthly_rental_income,
            "monthly_payment": self.loan_calculator.calculate_monthly_payment(
                self.property_total_value
            ),
            "loan_amount": self.property_total_value,
            "annual_rate": self.loan_calculator.annual_rate,
            "apport": self.loan_calculator.borrower.apport,
            "irr": round(irr, 2),
            "copro_fees": self.annual_coproperty_fees,
            "expenses": self.property_tax,
            "buy_price": self.buy_price,
            "management_fees": self.management_fees,
            "duration": self.holding_years,
            "works_price": self.works_price,
            "property_total_value": self.property_total_value,
        }
