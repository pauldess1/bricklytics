from borrower_profile import Profile

MAX_DEBT_TO_INCOME_RATIO = 0.33


class LoanCalculator:
    def __init__(
        self,
        loan_amount: int,
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
        self.loan_amount = loan_amount
        self.annual_rate = annual_rate
        self.years = years
        self.borrower = borrower_profile

    def calculate_max_loan_amount(self):
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
        return max_loan_amount

    def is_loan_affordable(self):
        """
        Checks if the loan is affordable based on the borrower's financial profile.
        :return: True if the loan is affordable, False otherwise.
        """
        max_loan_amount = self.calculate_max_loan_amount()
        return self.loan_amount <= max_loan_amount

    def calculate_monthly_payment(self):
        monthly_rate = self.annual_rate / 100 / 12
        number_of_payments = self.years * 12
        if monthly_rate == 0:
            return self.loan_amount / number_of_payments
        return (self.loan_amount * monthly_rate) / (
            1 - (1 + monthly_rate) ** -number_of_payments
        )

    def total_payment(self):
        return self.calculate_monthly_payment() * self.years * 12

    def total_interest(self):
        return self.total_payment() - self.loan_amount

    def display_loan_summary(self):
        monthly_payment = self.calculate_monthly_payment()
        total_payment = self.total_payment()
        total_interest = self.total_interest()

        summary = (
            f"Loan Summary:\n"
            f"Loan Amount: {self.loan_amount:.2f}€\n"
            f"Annual Interest Rate: {self.annual_rate:.2f}%\n"
            f"Years: {self.years}\n"
            f"Monthly Payment: {monthly_payment:.2f}€\n"
            f"Total Payment: {total_payment:.2f}€\n"
            f"Total Interest Paid: {total_interest:.2f}€"
        )
        return summary


if __name__ == "__main__":
    borrower = Profile(monthly_revenue=5000, monthly_expenses=1000, age=30)

    loan = LoanCalculator(
        loan_amount=180000, annual_rate=3.58, years=20, borrower_profile=borrower
    )
    print(loan.borrower.display_profile())
    print("##################################")
    print("Calculating loan affordability...")
    print(loan.calculate_max_loan_amount())
    print("##################################")

    if loan.is_loan_affordable():
        print(loan.display_loan_summary())
    else:
        print("This loan exceeds the authorized debt ratio.")
