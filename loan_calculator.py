class LoanCalculator:
    def __init__(self, capital, annual_rate, years):
        self.capital = capital
        self.annual_rate = annual_rate
        self.years = years

    def calculate_monthly_payment(self):
        monthly_rate = self.annual_rate / 100 / 12
        number_of_payments = self.years * 12
        if monthly_rate == 0:
            return self.capital / number_of_payments
        return (self.capital * monthly_rate) / (
            1 - (1 + monthly_rate) ** -number_of_payments
        )

    def total_payment(self):
        return self.calculate_monthly_payment() * self.years * 12

    def total_interest(self):
        return self.total_payment() - self.capital

    def display_loan_summary(self):
        monthly_payment = self.calculate_monthly_payment()
        total_payment = self.total_payment()
        total_interest = self.total_interest()

        summary = (
            f"Loan Summary:\n"
            f"capital: {self.capital:.2f}€\n"
            f"Annual Interest Rate: {self.annual_rate:.2f}%\n"
            f"Years: {self.years}\n"
            f"Monthly Payment: {monthly_payment:.2f}€\n"
            f"Total Payment: {total_payment:.2f}€\n"
            f"Total Interest Paid: {total_interest:.2f}€"
        )
        return summary


# Example usage:
if __name__ == "__main__":
    loan = LoanCalculator(capital=180000, annual_rate=3.58, years=20)
    print(loan.display_loan_summary())
