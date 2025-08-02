from borrower_profile import Profile

MAX_DEBT_TO_INCOME_RATIO = 0.33


class LoanCalculator:
    def __init__(
        self,
        annual_rate: float,
        years: int,
        borrower_profile: Profile,
    ):
        """
        Initializes the LoanCalculator with the loan parameters and borrower profile.
        :param loan_amount: The total amount of the loan in euros.
        :param annual_rate: The annual interest rate as a percentage.
        :param years: The duration of the loan in years.
        :param borrower_profile: An instance of Profile containing borrower's
                                    financial details.
        """

        self.annual_rate = annual_rate
        self.years = years
        self.borrower = borrower_profile

    def calculate_max_loan_amount(self) -> int:
        """
        Calculates the maximum loan amount based on the borrower's monthly revenue.
        :return: The maximum loan amount in euros.
        """
        max_mensuality = self.borrower.monthly_revenue * MAX_DEBT_TO_INCOME_RATIO
        monthly_ratio = self.annual_rate / 100 / 12
        max_loan_amount = (
            max_mensuality
            * (1 - (1 + monthly_ratio) ** -(self.years * 12))
            / monthly_ratio
        )
        return int(max_loan_amount)

    def is_loan_affordable(self, loan_amount: int) -> bool:
        """
        Checks if the loan is affordable based on the borrower's financial profile.
        :return: True if the loan is affordable, False otherwise.
        """
        max_loan_amount = self.calculate_max_loan_amount()
        return loan_amount <= max_loan_amount

    def calculate_monthly_payment(self, loan_amount: int) -> int:
        monthly_rate = self.annual_rate / 100 / 12
        number_of_payments = self.years * 12
        if monthly_rate == 0:
            return loan_amount / number_of_payments
        return int(
            (loan_amount * monthly_rate)
            / (1 - (1 + monthly_rate) ** -number_of_payments)
        )

    def total_payment(self, loan_amount: int) -> int:
        return self.calculate_monthly_payment(loan_amount) * self.years * 12

    def total_interest(self, loan_amount: int) -> int:
        return self.total_payment(loan_amount) - loan_amount

    def display_loan_summary(self, loan_amount: int) -> str:
        monthly_payment = self.calculate_monthly_payment(loan_amount)
        total_payment = self.total_payment(loan_amount)
        total_interest = self.total_interest(loan_amount)

        summary = (
            f"Loan Summary:\n"
            f"Loan Amount: {loan_amount:.2f}€\n"
            f"Annual Interest Rate: {self.annual_rate:.2f}%\n"
            f"Years: {self.years}\n"
            f"Monthly Payment: {monthly_payment:.2f}€\n"
            f"Total Payment: {total_payment:.2f}€\n"
            f"Total Interest Paid: {total_interest:.2f}€"
        )
        return summary
