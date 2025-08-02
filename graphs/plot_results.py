import streamlit as st
import plotly.graph_objects as go


def display_indicators(result: dict):
    st.subheader("📌 Indicateurs de performance")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("💰 Rentabilité brute", f"{result.get('gross_profitability', 0):.2f} %")
    col2.metric("💸 Rentabilité nette", f"{result.get('net_profitability', 0):.2f} %")
    col3.metric("📉 Cashflow mensuel", f"{result.get('monthly_cash_flow', 0):,.2f} €")
    col4.metric("📈 TRI (IRR)", f"{result.get('irr', 0):.2f} %")

    st.subheader("🏦 Détail du prêt accordé")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.markdown(
        f"<small>💵 Montant du prêt<br><b>{result.get('loan_amount', 0):,.0f} €</b></small>",
        unsafe_allow_html=True,
    )
    col2.markdown(
        f"<small>🏠 Apport personnel<br><b>{result.get('apport', 0):,.0f} €</b></small>",
        unsafe_allow_html=True,
    )
    col3.markdown(
        f"<small>📅 Durée<br><b>{result.get('duration', 0)} ans</b></small>",
        unsafe_allow_html=True,
    )
    col4.markdown(
        f"<small>📈 Taux annuel<br><b>{result.get('annual_rate', 0):.2f} %</b></small>",
        unsafe_allow_html=True,
    )
    col5.markdown(
        f"<small>💳 Mensualité<br><b>{result.get('monthly_payment', 0):,.2f} €</b></small>",
        unsafe_allow_html=True,
    )


def display_amortization_chart(result: dict):
    st.markdown("### 📘 Capital remboursé vs Épargne personnelle")
    duration = result.get("duration", 20)
    years = list(range(0, duration + 1))

    mensualite = result.get("monthly_payment", 0)
    cashflow = result.get("monthly_cash_flow", 0)
    property_total_value = result.get(
        "property_total_value", result.get("buy_price", 0)
    )
    apport = result.get("apport", 0)

    # Capital remboursé linéairement sur la durée (approximation)
    capital_rembourse = [property_total_value * (i / duration) for i in years]

    # Total remboursé cumulatif (mensualité * 12 * années)
    total_rembourse = [mensualite * 12 * i for i in years]

    # Effort d’épargne cumulatif selon cashflow
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
        margin=dict(t=50, b=50, l=40, r=40),
    )

    st.plotly_chart(fig, use_container_width=True)


def display_chart(result: dict):
    st.subheader("📊 Visualisations")

    st.markdown(
        "### 💡 Comparaison simple : Loyer perçu vs Total des dépenses mensuelles"
    )

    rent = result.get("monthly_rent", 0)
    mensualite = result.get("monthly_payment", 0)
    expenses = result.get("expenses", 0)
    copro_fees = result.get("copro_fees", 0)
    management_fees_percent = result.get("management_fees", 0)

    charges_fixes = (expenses + copro_fees) / 12
    gestion = rent * management_fees_percent / 100
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
        margin=dict(t=50, b=50, l=40, r=40),
    )

    st.plotly_chart(fig_comp, use_container_width=True)
