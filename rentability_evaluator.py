import numpy_financial as npf


class Evaluator:
    """
    Evaluates the financial viability of a real estate investment.
    """

    def __init__(
        self,
        buy_price,
        monthly_rental_income,
        expenses,
        annual_coproperty_fees,
        loan_calculator,
        management_fees=0,
        holding_years=20,
        resale_value=None,
    ):
        self.buy_price = buy_price
        self.monthly_rental_income = monthly_rental_income
        self.property_tax = expenses
        self.annual_coproperty_fees = annual_coproperty_fees
        self.loan_calculator = loan_calculator
        self.management_fees = management_fees
        self.holding_years = holding_years
        self.resale_value = resale_value or buy_price * (1.02**holding_years)

    def calculate_monthly_cash_flow(self):
        """
        Calculates the monthly cash flow from the rental property.
        :return: Monthly cash flow in euros.
        """
        monthly_expenses = (
            self.property_tax / 12
            + self.annual_coproperty_fees / 12
            + self.management_fees
            + self.loan_calculator.calculate_monthly_payment(self.buy_price)
        )
        return self.monthly_rental_income - monthly_expenses

    def calculate_irr(self):
        """
        Calculates the Internal Rate of Return (IRR) of the investment.
        """
        monthly_cashflow = self.calculate_monthly_cash_flow()
        nb_months = self.holding_years * 12

        cash_flows = [-self.loan_calculator.borrower.apport]
        cash_flows += [monthly_cashflow] * nb_months
        cash_flows[-1] += self.resale_value

        irr = npf.irr(cash_flows)
        return irr * 12 * 100

    def evaluate_rentability(self):
        """
        Returns key financial indicators of the investment.
        """
        gross_profitability = (self.monthly_rental_income * 12 / self.buy_price) * 100

        net_profitability = (
            self.calculate_monthly_cash_flow() * 12 / self.buy_price
        ) * 100

        irr = self.calculate_irr()

        return {
            "gross_profitability": round(gross_profitability, 2),
            "net_profitability": round(net_profitability, 2),
            "monthly_cash_flow": round(self.calculate_monthly_cash_flow(), 2),
            "irr": round(irr, 2),
        }
