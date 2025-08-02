from borrower_profile import Profile
from loan_calculator import LoanCalculator
from rentability_evaluator import Evaluator


def main():
    # Create borrower profile with apport
    profile = Profile(age=32, monthly_revenue=4000, monthly_expenses=500, apport=5000)
    print(profile.display_profile())

    # Setup loan calculator (interest rate and duration)
    loan = LoanCalculator(annual_rate=3.58, years=20, borrower_profile=profile)

    # Setup property and evaluator
    evaluator = Evaluator(
        buy_price=140000,
        monthly_rental_income=900,
        expenses=1200,  # property tax yearly
        annual_coproperty_fees=600,
        loan_calculator=loan,
        management_fees=0,
        holding_years=20,
    )

    # Evaluate investment
    result = evaluator.evaluate_rentability()
    print(result)


if __name__ == "__main__":
    main()
