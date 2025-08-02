class Profile:
    def __init__(self, monthly_revenue, monthly_expenses, age):
        self.monthly_revenue = monthly_revenue
        self.monthly_expenses = monthly_expenses
        self.age = age

    def display_profile(self):
        profile_info = (
            f"Profile Information:\n"
            f"Monthly Revenue: {self.monthly_revenue:.2f}€\n"
            f"Age: {self.age} years"
        )
        return profile_info
