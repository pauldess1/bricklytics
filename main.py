import tkinter as tk
from tkinter import ttk, messagebox

from borrower_profile import Profile
from loan_calculator import LoanCalculator
from rentability_evaluator import Evaluator


class InvestmentApp:
    def __init__(self, root):
        self.root = root
        root.title("Simulateur Investissement Locatif")
        self.create_widgets()

    def create_widgets(self):
        padding = {"padx": 10, "pady": 5}

        # Profil emprunteur
        tk.Label(text="Âge").grid(row=0, column=0, **padding)
        self.age_entry = tk.Entry()
        self.age_entry.grid(row=0, column=1, **padding)

        tk.Label(text="Revenu Mensuel (€)").grid(row=1, column=0, **padding)
        self.revenue_entry = tk.Entry()
        self.revenue_entry.grid(row=1, column=1, **padding)

        tk.Label(text="Apport (€)").grid(row=2, column=0, **padding)
        self.apport_entry = tk.Entry()
        self.apport_entry.grid(row=2, column=1, **padding)

        # Bien
        tk.Label(text="Prix du bien (€)").grid(row=3, column=0, **padding)
        self.price_entry = tk.Entry()
        self.price_entry.grid(row=3, column=1, **padding)

        tk.Label(text="Loyer mensuel (€)").grid(row=4, column=0, **padding)
        self.rent_entry = tk.Entry()
        self.rent_entry.grid(row=4, column=1, **padding)

        tk.Label(text="Taxe foncière annuelle (€)").grid(row=5, column=0, **padding)
        self.tax_entry = tk.Entry()
        self.tax_entry.grid(row=5, column=1, **padding)

        tk.Label(text="Frais copropriété annuels (€)").grid(row=6, column=0, **padding)
        self.copro_entry = tk.Entry()
        self.copro_entry.grid(row=6, column=1, **padding)

        # Crédit
        tk.Label(text="Taux annuel (%)").grid(row=7, column=0, **padding)
        self.rate_entry = tk.Entry()
        self.rate_entry.grid(row=7, column=1, **padding)

        tk.Label(text="Durée du prêt (années)").grid(row=8, column=0, **padding)
        self.duration_entry = tk.Entry()
        self.duration_entry.grid(row=8, column=1, **padding)

        # Bouton
        self.calc_button = ttk.Button(
            text="Évaluer Rentabilité", command=self.calculate
        )
        self.calc_button.grid(row=9, column=0, columnspan=2, pady=10)

        # Résultat
        self.result_text = tk.Text(height=10, width=60)
        self.result_text.grid(row=10, column=0, columnspan=2, **padding)

    def calculate(self):
        try:
            # Profil
            profile = Profile(
                age=int(self.age_entry.get()),
                monthly_revenue=float(self.revenue_entry.get()),
                apport=float(self.apport_entry.get()),
            )

            # Prêt
            loan = LoanCalculator(
                annual_rate=float(self.rate_entry.get()),
                years=int(self.duration_entry.get()),
                borrower_profile=profile,
            )

            # Simulation
            evaluator = Evaluator(
                buy_price=float(self.price_entry.get()),
                monthly_rental_income=float(self.rent_entry.get()),
                expenses=float(self.tax_entry.get()),
                annual_coproperty_fees=float(self.copro_entry.get()),
                loan_calculator=loan,
                management_fees=0,
                holding_years=int(self.duration_entry.get()),
            )

            result = evaluator.evaluate_rentability()
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue :\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = InvestmentApp(root)
    root.mainloop()
