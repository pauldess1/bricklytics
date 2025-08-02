from borrower_profile import Profile

MAX_DEBT_TO_INCOME_RATIO = 0.33


class LoanCalculator:
    """
    Calculate loan parameters and check affordability based on borrower profile.
    """

    def __init__(self, annual_rate: float, years: int, borrower_profile: Profile):
        """
        :param annual_rate: Annual interest rate in percentage (e.g. 3.5 for 3.5%)
        :param years: Loan duration in years
        :param borrower_profile: Borrower's financial profile (income, apport, etc.)
        """
        self.annual_rate = annual_rate
        self.years = years
        self.borrower = borrower_profile

    def calculate_max_loan_amount(self) -> int:
        """
        Calculate the maximum loan amount affordable by the borrower
        based on a maximum debt-to-income ratio.
        """
        max_monthly_payment = self.borrower.monthly_revenue * MAX_DEBT_TO_INCOME_RATIO
        monthly_rate = self.annual_rate / 100 / 12
        nb_payments = self.years * 12

        if monthly_rate == 0:
            max_loan = max_monthly_payment * nb_payments
        else:
            max_loan = (
                max_monthly_payment
                * (1 - (1 + monthly_rate) ** -nb_payments)
                / monthly_rate
            )

        return int(max_loan)

    def is_loan_affordable(self, loan_amount: int) -> bool:
        """
        Check if the requested loan amount is affordable for the borrower.
        """
        return loan_amount <= self.calculate_max_loan_amount()

    def calculate_monthly_payment(self, loan_amount: int) -> int:
        """
        Calculate the fixed monthly payment for a given loan amount.
        """
        monthly_rate = self.annual_rate / 100 / 12
        nb_payments = self.years * 12

        if monthly_rate == 0:
            payment = loan_amount / nb_payments
        else:
            payment = (loan_amount * monthly_rate) / (
                1 - (1 + monthly_rate) ** -nb_payments
            )

        return int(payment)

    def total_payment(self, loan_amount: int) -> int:
        """
        Total amount paid over the entire loan period (principal + interest).
        """
        return self.calculate_monthly_payment(loan_amount) * self.years * 12

    def total_interest(self, loan_amount: int) -> int:
        """
        Total interest paid over the loan duration.
        """
        return self.total_payment(loan_amount) - loan_amount

    def display_loan_summary(self, loan_amount: int) -> str:
        """
        Returns a formatted summary of the loan details.
        """
        monthly_payment = self.calculate_monthly_payment(loan_amount)
        total_payment = self.total_payment(loan_amount)
        total_interest = self.total_interest(loan_amount)

        return (
            f"Loan Summary:\n"
            f"Loan Amount: {loan_amount:.2f} €\n"
            f"Annual Interest Rate: {self.annual_rate:.2f} %\n"
            f"Duration: {self.years} years\n"
            f"Monthly Payment: {monthly_payment:.2f} €\n"
            f"Total Payment: {total_payment:.2f} €\n"
            f"Total Interest Paid: {total_interest:.2f} €"
        )
