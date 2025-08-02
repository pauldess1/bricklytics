class Profile:
    def __init__(self, monthly_revenue, age, apport):
        self.monthly_revenue = monthly_revenue
        self.age = age
        self.apport = apport

    def display_profile(self):
        profile_info = (
            f"Profile Information:\n"
            f"Monthly Revenue: {self.monthly_revenue:.2f}€\n"
            f"Age: {self.age} years\n"
            f"Apport (Down Payment): {self.apport:.2f}€"
        )
        return profile_info

    def __repr__(self):
        return (
            f"Profile(revenue={self.monthly_revenue}€, "
            f"age={self.age}, apport={self.apport}€)"
        )
