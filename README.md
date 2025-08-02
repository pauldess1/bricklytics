# 🧱 Bricklytics

**Bricklytics** est un outil d’aide à la décision pour l’investissement locatif.  
Il permet de simuler la capacité d’emprunt, d’évaluer la rentabilité d’un bien immobilier, et de visualiser les indicateurs financiers clés pour guider l’investisseur.

Son objectif : **aider rapidement à estimer la viabilité d’un projet immobilier**, en fonction du profil financier de l’utilisateur et des caractéristiques du bien.

---

## 🚀 Fonctionnalités

- 🧮 **Calcul de capacité d’emprunt** selon le revenu, l’âge, l’apport, le taux et la durée.
- 📉 **Simulation de prêt** avec mensualités, intérêts, et échéancier d’amortissement.
- 📊 **Évaluation de rentabilité** (brute, nette, cashflow mensuel, TRI).
- 📈 **Visualisation graphique** des flux financiers et de l’effort d’épargne.
- 💡 **Outil complet de simulation financière** pour les investisseurs particuliers.

---

## 📁 Structure du projet

```
bricklytics/
│
├── core/
│   ├── borrower_profile.py
│   ├── loan_calculator.py 
│   ├── rentability_evaluator.py
│
├── app/
│   ├── interface.py
│   ├── plot_results.py
│
├── tests/
├── main.py 
└── README.md
```

---

## 🔧 Exécution de l'outil

### 1. Installation

```bash
git clone https://github.com/pauldess1/bricklytics.git
cd bricklytics
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Lancer l’application Streamlit

```bash
streamlit run main.py
```

---

## 🗺️ Roadmap

### ✅ Phase 1 – Core financier

- Création du profil utilisateur
- Calcul du montant d'emprunt maximal
- Simulation du prêt et mensualités

### ✅ Phase 2 – Évaluation financière

- Calcul du cashflow
- Rentabilité brute et nette
- Calcul du TRI
- Visualisations Streamlit

### 🔜 Phase 3 – Interface & automatisation

- Amélioration de l’interface Streamlit
- Génération de rapports PDF
- Scénarios alternatifs et simulations comparatives