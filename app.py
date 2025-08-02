import streamlit as st
from borrower_profile import Profile
from loan_calculator import LoanCalculator
from rentability_evaluator import Evaluator
from graphs.plot_results import (
    display_indicators,
    display_chart,
    display_amortization_chart,
)


def app():
    NOTARY_FEES_PERCENT = 8  # Pourcentage frais de notaire

    st.title("🏠 Simulateur d'investissement locatif")

    # Profil de l'emprunteur
    st.sidebar.header("Profil de l’emprunteur")
    age = st.sidebar.number_input("Âge", min_value=18, value=30)
    monthly_revenue = st.sidebar.number_input(
        "Revenu mensuel (€)", min_value=0, value=4000
    )
    apport = st.sidebar.number_input("Apport disponible (€)", min_value=0, value=10000)

    # Conditions du prêt
    st.sidebar.header("Conditions du prêt")
    annual_rate = st.sidebar.number_input(
        "Taux annuel (%)", min_value=0.0, value=3.5, step=0.1
    )
    duration_years = st.sidebar.slider(
        "Durée du prêt (années)", min_value=5, max_value=30, value=20
    )

    # Informations sur le bien
    st.header("Informations sur le bien")
    buy_price = st.number_input("Prix d’achat (€)", min_value=0, value=140000)
    notary_fees_included = st.checkbox(
        "Frais de notaire inclus dans le prix de vente", value=True
    )
    works_price = st.number_input(
        "Coût des travaux (€)",
        min_value=0,
        value=0,
        help="Coût estimé des travaux à réaliser",
    )
    monthly_rent = st.number_input("Loyer mensuel espéré (€)", min_value=0, value=850)
    property_tax = st.number_input(
        "Taxe foncière annuelle (€)", min_value=0, value=1000
    )
    copro_fees = st.number_input(
        "Charges de copropriété annuelles (€)", min_value=0, value=500
    )
    management_fees_percent = st.slider(
        "Frais de gestion (%)", min_value=0, max_value=20, value=0
    )

    if st.button("📊 Évaluer la rentabilité"):
        try:
            # Profil emprunteur
            profile = Profile(age=age, monthly_revenue=monthly_revenue, apport=apport)
            loan = LoanCalculator(
                annual_rate=annual_rate,
                years=duration_years,
                borrower_profile=profile,
            )

            # Ajustement du prix d'achat si frais de notaire non inclus
            total_buy_price = buy_price
            if not notary_fees_included:
                total_buy_price = buy_price * (1 + NOTARY_FEES_PERCENT / 100)

            # Création de l'évaluateur
            evaluator = Evaluator(
                buy_price=total_buy_price,
                monthly_rental_income=monthly_rent,
                property_tax=property_tax,
                annual_coproperty_fees=copro_fees,
                loan_calculator=loan,
                works_price=works_price,
                management_fees=management_fees_percent
                / 100
                * monthly_rent,  # convert %
                holding_years=duration_years,
            )

            result = evaluator.evaluate_rentability()

            st.success("Évaluation réussie 🎉")
            display_indicators(result)
            display_chart(result)
            display_amortization_chart(result)

        except Exception as e:
            st.error(f"Erreur lors du calcul : {e}")


if __name__ == "__main__":
    app()
