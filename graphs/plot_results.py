import streamlit as st
import plotly.graph_objects as go


def display_indicators(result: dict):
    st.subheader("📌 Résultats principaux")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("💰 Rentabilité brute", f"{result['gross_profitability']} %")
    col2.metric("💸 Rentabilité nette", f"{result['net_profitability']} %")
    col3.metric("📉 Cashflow mensuel", f"{result['monthly_cash_flow']} €")
    col4.metric("📈 TRI (IRR)", f"{result['irr']} %")


def display_chart(result: dict):
    st.subheader("📊 Visualisations")

    # === 1. Loyer vs Sorties mensuelles ===
    st.markdown(
        "### 💡 Comparaison simple : Loyer perçu vs Total des dépenses mensuelles"
    )

    rent = result["monthly_rent"]
    mensualite = result["monthly_payment"]
    charges_fixes = (result["expenses"] + result["copro_fees"]) / 12
    gestion = rent * result["management_fees"] / 100
    total_sorties = mensualite + charges_fixes + gestion

    fig_comp = go.Figure()
    fig_comp.add_trace(
        go.Bar(
            name="Loyer mensuel",
            x=["Investissement locatif"],
            y=[rent],
            marker_color="green",
        )
    )
    fig_comp.add_trace(
        go.Bar(
            name="Sorties totales mensuelles",
            x=["Investissement locatif"],
            y=[total_sorties],
            marker_color="crimson",
        )
    )

    fig_comp.update_layout(
        barmode="group",
        title="Loyer perçu vs total des dépenses",
        yaxis_title="Montant (€)",
        xaxis_title="",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
    )

    st.plotly_chart(fig_comp, use_container_width=True)


def display_amortization_chart(result: dict):
    st.markdown("### 📘 Capital remboursé vs Épargne personnelle")
    duration = result["duration"]
    years = list(range(0, duration + 1))  # Commence à 0 maintenant

    mensualite = result["monthly_payment"]
    cashflow = result["monthly_cash_flow"]
    buy_price = result["buy_price"]
    apport = result["apport"]  # assure-toi de l’inclure dans result

    # Capital remboursé : commence à 0 jusqu'à buy_price
    capital_rembourse = [buy_price * (i / duration) for i in years]

    # Coût total du prêt : commence à 0 jusqu’à mensualité*12*duration
    total_rembourse = [mensualite * 12 * i for i in years]

    # Épargne personnelle : commence à apport uniquement
    if cashflow < 0:
        effort_epargne = [apport + abs(cashflow) * 12 * i for i in years]
    else:
        effort_epargne = [apport] * (duration + 1)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=years,
            y=total_rembourse,
            mode="lines+markers",
            name="Coût total du prêt",
            line=dict(color="blue"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=years,
            y=capital_rembourse,
            mode="lines+markers",
            name="Mon capital",
            line=dict(color="green"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=years,
            y=effort_epargne,
            mode="lines+markers",
            name="Épargne personnelle",
            line=dict(color="red", dash="dash"),
        )
    )

    fig.update_layout(
        title="Évolution du patrimoine net (capital vs épargne)",
        xaxis_title="Année",
        yaxis_title="Montant cumulé (€)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
    )

    st.plotly_chart(fig, use_container_width=True)
