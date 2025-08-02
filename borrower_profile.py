class Profile:
    def __init__(self, monthly_revenue, monthly_expenses, age, apport):
        self.monthly_revenue = monthly_revenue
        self.monthly_expenses = monthly_expenses
        self.age = age
        self.apport = apport

    def display_profile(self):
        profile_info = (
            f"Profile Information:\n"
            f"Monthly Revenue: {self.monthly_revenue:.2f}€\n"
            f"Monthly Expenses: {self.monthly_expenses:.2f}€\n"
            f"Age: {self.age} years\n"
            f"Apport (Down Payment): {self.apport:.2f}€"
        )
        return profile_info

    def __repr__(self):
        return (
            f"Profile(revenue={self.monthly_revenue}€, "
            f"expenses={self.monthly_expenses}€, "
            f"age={self.age}, apport={self.apport}€)"
        )
