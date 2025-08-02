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
    notary_fees = 8
    st.title("🏠 Simulateur d'investissement locatif")

    # Profil emprunteur
    st.sidebar.header("Profil de l’emprunteur")
    age = st.sidebar.number_input("Âge", min_value=18, value=30)
    monthly_revenue = st.sidebar.number_input("Revenu mensuel (€)", value=4000)
    apport = st.sidebar.number_input("Apport disponible (€)", value=10000)

    # Conditions de prêt
    st.sidebar.header("Conditions du prêt")
    rate = st.sidebar.number_input("Taux annuel (%)", value=3.5)
    duration = st.sidebar.slider("Durée du prêt (années)", 5, 30, value=20)

    # Informations sur le bien
    st.header("Informations sur le bien")
    buy_price = st.number_input("Prix d’achat (€)", value=140000)
    notary_fees_included = st.checkbox(
        "Frais de notaire inclus dans le prix de vente", value=True
    )
    monthly_rent = st.number_input("Loyer mensuel espéré (€)", value=850)
    property_tax = st.number_input("Taxe foncière annuelle (€)", value=1000)
    copro_fees = st.number_input("Charges de copropriété annuelles (€)", value=500)
    management_fees = st.slider("Frais de gestion (%)", 0, 20, value=0)

    # Bouton de calcul
    if st.button("📊 Évaluer la rentabilité"):
        try:
            profile = Profile(age=age, monthly_revenue=monthly_revenue, apport=apport)
            loan = LoanCalculator(
                annual_rate=rate, years=duration, borrower_profile=profile
            )
            if not notary_fees_included:
                buy_price = buy_price * (1 + notary_fees / 100)
            evaluator = Evaluator(
                buy_price=buy_price,
                monthly_rental_income=monthly_rent,
                property_tax=property_tax,
                annual_coproperty_fees=copro_fees,
                loan_calculator=loan,
                management_fees=management_fees,
                holding_years=duration,
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
